# JARVIS SDLC

JARVIS SDLC is a local-first, multi-agent software engineering system intended to support the full software lifecycle under human supervision.

The project is being built incrementally. Specialized agents will not be defined from generic prompts: each specialty will be researched, specified, tested, and versioned before it becomes part of the system.

## Core direction

- Human supervisor, autonomous orchestration.
- Specialized agents with clear boundaries and handoffs.
- Evidence over authority or assumptions.
- For existing projects: understand documentation and intended behavior before judging the implementation.
- Distinguish intended system, implemented system, and observed runtime behavior.
- Do not accept user statements, documentation, tests, or code as automatically correct; verify and reconcile evidence.
- Escalate to the supervisor when real-world information, authority, or unresolved ambiguity is required.
- Local-first execution on Ubuntu.
- Initial AI runtime: Claude Code authenticated through Claude Pro, without paid API usage.
- Web research is not treated as truth by default; sources must be evaluated before being incorporated.

## Initial milestone

The first end-to-end workflow will be:

`AUDIT_EXISTING_PROJECT`

Its purpose is to take an existing software project, reconstruct what it is supposed to do from its available documentation and artifacts, inspect the implementation and runtime behavior, identify discrepancies and defects, investigate likely causes, and produce evidence-backed findings.

## Status

Bootstrap phase.
