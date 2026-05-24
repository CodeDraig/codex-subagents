# Prompt Injection Defense Checklist

## Control Layers

- Treat external content as data, never instructions.
- Keep system/developer instructions out of retrievable context.
- Use tool allowlists and scoped credentials.
- Validate tool arguments with schemas and policy checks.
- Require confirmation for external side effects.
- Separate read-only analysis from write actions.
- Log decisions and tool calls without leaking secrets.

## Test Attacks

- "Ignore previous instructions."
- Data asking model to reveal hidden prompts.
- Malicious retrieved document requesting tool calls.
- Conflicting user and document authority.
- Exfiltration through summaries, URLs, or code.
- Indirect injection in email, ticket, webpage, PDF, or repository file.
