# Security Policy

## What this project is

Prism Council is a set of Markdown instructions for AI coding agents. Installing it runs no code. `scripts/check_repo.py` is a development check and is not installed by `npx skills`.

## Risks to know about

- **Your brief goes to your model provider.** The council sends a short summary of your decision to the subagents your host spawns. The same provider your agent already uses processes it. Do not run the council on material you are not allowed to send to that provider.
- **Seats can read files.** In isolated mode, insider seats may read up to 3 workspace files. The skill tells them never to edit anything, but enforcement depends on your host's tool permissions. The optional Claude Code adapter restricts tools explicitly.
- **Skills run with your agent's permissions.** Review any skill before you install it, including this one.

## Reporting a vulnerability

If you find a way the instructions could cause harmful actions, report it privately through [GitHub private vulnerability reporting](https://github.com/ehsandaryaei/prism-council/security/advisories/new). An example is prompt injection through the brief that makes a seat edit files or leak data. Please do not open a public issue for it.

Expect a first response within 7 days.
