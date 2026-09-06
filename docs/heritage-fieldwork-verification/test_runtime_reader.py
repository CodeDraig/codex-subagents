"""Exercise the discovery harness's exact reader without executing its setup."""
import ast
import io
import json
import os
from pathlib import Path
import selectors
import threading
import time
from types import SimpleNamespace
import unittest

SOURCE = Path(__file__).with_name('runtime_check.py')


def load_reader(proc, selector):
    node = next(n for n in ast.parse(SOURCE.read_text()).body
                if isinstance(n, ast.FunctionDef) and n.name == 'request')
    scope = dict(json=json, os=os, time=time, proc=proc, selector=selector,
                 messages=[], pending_output=b'')
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE), 'exec'), scope)
    return scope


class ReaderTests(unittest.TestCase):
    def setUp(self):
        read_fd, self.write_fd = os.pipe()
        self.stdout = os.fdopen(read_fd, 'r')
        self.selector = selectors.DefaultSelector()
        self.selector.register(self.stdout, selectors.EVENT_READ)
        self.scope = load_reader(SimpleNamespace(stdin=io.StringIO(), stdout=self.stdout), self.selector)

    def tearDown(self):
        self.selector.close()
        self.stdout.close()
        if self.write_fd is not None:
            os.close(self.write_fd)

    def request(self, number=1):
        return self.scope['request'](number, 'test', {}, timeout=0.1)

    def test_coalesced_notifications_error_and_next_response(self):
        frames = [{'method': 'notice'}, {'id': 1, 'error': {'code': -32603}},
                  {'method': 'another'}, {'id': 2, 'result': 'ok'}]
        os.write(self.write_fd, b''.join(json.dumps(m).encode() + b'\n' for m in frames))
        # Keep the writer open: EOF readiness would hide the original buffer bug.
        with self.assertRaises(RuntimeError) as raised:
            self.request()
        self.assertEqual(raised.exception.args[0], {'code': -32603})
        self.assertEqual(self.request(2), 'ok')
        self.assertEqual(self.scope['messages'], frames)

    def test_fragmented_utf8(self):
        payload = json.dumps({'id': 1, 'result': 'café'}, ensure_ascii=False).encode() + b'\n'
        split = payload.index(b'\xc3') + 1
        os.write(self.write_fd, payload[:split])
        writer = threading.Thread(target=lambda: (time.sleep(0.02), os.write(self.write_fd, payload[split:])))
        writer.start()
        try:
            self.assertEqual(self.request(), 'café')
        finally:
            writer.join()

    def test_partial_frame_deadline_and_resume(self):
        os.write(self.write_fd, b'{"id":1,"result":')
        start = time.monotonic()
        with self.assertRaises(TimeoutError):
            self.request()
        self.assertLess(time.monotonic() - start, 0.5)
        os.write(self.write_fd, b'"complete"}\n')
        self.assertEqual(self.request(), 'complete')

    def test_eof_with_partial_frame(self):
        os.write(self.write_fd, b'{"id":')
        os.close(self.write_fd)
        self.write_fd = None
        with self.assertRaisesRegex(RuntimeError, 'app-server exited'):
            self.request()

    def test_complete_reply_before_eof(self):
        os.write(self.write_fd, b'{"method":"notice"}\n{"id":1,"result":true}\n')
        os.close(self.write_fd)
        self.write_fd = None
        self.assertTrue(self.request())


if __name__ == '__main__':
    unittest.main()
