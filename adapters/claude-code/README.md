# Claude Code adapter (optional)

The skill works in Claude Code without this adapter: it runs each seat as a general-purpose subagent with the seat rules embedded in the prompt.

These two agent definitions add two things the portable skill cannot express:

- **Model pinning.** Both agents use `model: sonnet`, so a council run costs about 5 Sonnet calls even when your main session runs a larger model. The skill's `--deep` flag still asks for the strongest model.
- **Tool restriction.** Seats get read-only tools (`Read, Grep, Glob`). The Outsider gets only `Read` and is told not to use it.

When these agents exist, the skill uses them automatically (it looks for `council-member` and `council-outsider`).

## Install

`npx skills` installs skills only, not agent definitions, so copy these files by hand.

macOS / Linux:

```bash
mkdir -p ~/.claude/agents
curl -fsSL -o ~/.claude/agents/council-member.md https://raw.githubusercontent.com/ehsandaryaei/prism-council/main/adapters/claude-code/agents/council-member.md
curl -fsSL -o ~/.claude/agents/council-outsider.md https://raw.githubusercontent.com/ehsandaryaei/prism-council/main/adapters/claude-code/agents/council-outsider.md
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\agents" | Out-Null
foreach ($f in "council-member.md", "council-outsider.md") {
  Invoke-WebRequest "https://raw.githubusercontent.com/ehsandaryaei/prism-council/main/adapters/claude-code/agents/$f" -OutFile "$HOME\.claude\agents\$f"
}
```

Use `.claude/agents/` inside a project instead of `~/.claude/agents/` to scope them to one repository. Restart Claude Code, then check that `/agents` lists both.

Other hosts (Codex, Cursor, Gemini CLI, GitHub Copilot) define custom agents in their own formats. No adapter is shipped for them yet; the skill falls back to their general-purpose subagents.
