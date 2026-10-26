# Contributing

Thanks for helping improve Prism Council. This is a small, instruction-only project, so most contributions are edits to Markdown.

## Good contributions

- A host where the skill misbehaves, with the host name and version, the prompt you used, and what went wrong.
- Changes to the seat lenses or output formats that make verdicts sharper or cheaper, with one before/after example.
- Adapters for hosts that support custom agents (for example Codex, Cursor, Gemini CLI, Copilot), following [adapters/claude-code](adapters/claude-code/README.md).
- Fixes to the English or Persian documentation. Keep both languages aligned in meaning.

## Ground rules

- Keep `skills/prism-council/SKILL.md` portable. Do not add instructions that only work in one host; put those in `adapters/<host>/`.
- Keep `SKILL.md` short. The agent loads every line of it on each run.
- Do not claim compatibility you have not tested. Say "tested", "documented", or "untested".
- Do not include real conversations, company data, or secrets in examples.

## Before you open a pull request

```bash
pip install skills-ref
agentskills validate skills/prism-council
python scripts/check_repo.py
npx skills add . --list
```

CI runs the same checks. Add a line to [CHANGELOG.md](CHANGELOG.md) under an `Unreleased` heading.

## Reporting bugs and ideas

Use the [issue tracker](https://github.com/ehsandaryaei/prism-council/issues). For security problems, see [SECURITY.md](SECURITY.md).

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE) and that you will follow the [Code of Conduct](CODE_OF_CONDUCT.md).
