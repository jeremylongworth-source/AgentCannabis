# Agent Routing

AgentCannabis includes root routing templates modeled after the AgentSkills convention.

## Files

| File | Purpose |
| --- | --- |
| `agents/AGENTS.base.md` | Shared base instructions and safety boundaries |
| `agents/AGENTS.full.md` | Full routing across all 18 professional skillsets |
| `agents/AGENTS.<skillset>.md` | Focused routing for one professional role package |

## When to use root routing files

Use the root `agents/` files when configuring Codex-style or other local agent hosts that read project instructions directly. They are useful when the agent has access to the repository clone and can load `skills/` folders as needed.

Use `gh skill install` when the target host expects installed GitHub Copilot Agent Skills in a destination project.

## Regeneration

Routing files are generated from the existing professional skillset manifests and wrapper skill text:

```powershell
python scripts/generate_agent_routing_templates.py
```

Validation requires these files to exist and route every professional skillset:

```powershell
python scripts/validate_repository.py --stage full
```

Release `v1.0.4` includes base, full, and 18 professional routing templates.
