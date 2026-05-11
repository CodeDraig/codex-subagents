# UX State Table

| State | Trigger | User Sees | User Can Do | System Does | Notes |
| --- | --- | --- | --- | --- | --- |
| Loading | request starts | progress indication | wait/cancel if safe | fetch data | avoid layout shift |
| Empty | no items | empty-state message | create/import/search | no-op | explain next action |
| Error | recoverable failure | error message | retry/change input/contact | log safely | preserve user work |
| Permission denied | forbidden action | access message | request access/go back | block action | avoid leaking data |
| Success | completion | confirmation/state update | continue/undo if needed | persist | make result visible |

## Copy Rules

- State what happened.
- State what the user can do next.
- Avoid blaming the user.
- Keep destructive confirmations specific.
