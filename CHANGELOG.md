# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-26

First public release.

### Added
- `prism-council` skill in the Agent Skills format (`skills/prism-council/SKILL.md`).
- Two execution modes: isolated subagents when the host supports them, and a labeled single-context fallback.
- `--single` flag to force single-context mode.
- Optional Claude Code adapter (`adapters/claude-code/`) that pins seats to Sonnet and restricts their tools.
- Bilingual README (English and Persian), a sample run, a validation script, and a CI workflow.

### Changed (from the private `council` skill this release is based on)
- Seat and Outsider rules now live inside the prompts, so the skill no longer depends on Claude-only agent types.
- `--deep` asks for the host's strongest model instead of naming a Claude model.
- The relay states which mode ran.
