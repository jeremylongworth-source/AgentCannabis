# Agent Routing

AgentCannabis includes root routing templates modeled after the AgentSkills
project-instruction convention. They are useful when an agent can read the
repository clone directly and you want routing behavior without installing
every package into a host-specific directory.

## Files

| File | Purpose |
| --- | --- |
| `agents/AGENTS.base.md` | Shared routing, evidence discipline, and safety boundaries |
| `agents/AGENTS.full.md` | Full routing across all 18 professional skillsets |
| `agents/AGENTS.<skillset>.md` | Focused routing for one professional role package |

## Selecting a route

Use `AGENTS.base.md` for a minimal project boundary. Use `AGENTS.full.md` when
the agent should choose among all professional packages. Use a focused file
when the project has one dominant role:

```text
agents/AGENTS.cannabis-quality-systems-specialist.md
        |
        v
skills/cannabis-quality-systems-specialist/SKILL.md
        |
        v
references/member-index.json -> selected atomic workflows
```

The focused files do not replace the skill package. They route the request;
the selected `SKILL.md` and its references remain the runtime instructions.

## When to use GitHub CLI instead

Use `gh skill install` when the target host expects installed Agent Skills in a
destination project or user scope. Use the root routing files when the agent
already has repository access and should load packages progressively.

## Regeneration

Routing files are generated from the professional manifests and wrapper text:

```powershell
python scripts/generate_agent_routing_templates.py
```

Validate that every professional package has a routing file:

```powershell
python scripts/validate_repository.py --stage full
```

Release `v1.0.5` includes base, full, and 18 focused routing templates.
