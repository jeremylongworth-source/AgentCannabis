# Developer Guide

This page is for maintainers changing AgentCannabis locally. The repository
itself is execution truth; `ROADMAP.md`, the frozen taxonomy, the architecture
contracts, and the current wave evidence define what a change may touch.

## Before editing

Read `AGENTS.md`, `ROADMAP.md`, the latest final audit, the affected contract
under `docs/architecture/`, and the relevant authoring or testing standard.
Keep the frozen 233-skill taxonomy and the repository safety boundaries in
view. Do not mass-author skills before the CC-10 reference-skill gate is
closed.

## Common commands

Import the supplied taxonomy source. Replace the placeholder with the path to
your local copy:

```powershell
python scripts/import_taxonomy.py --source "D:\Sources\Taxonomy Canadian Cannabis Skill Repositor.txt" --output docs/architecture/taxonomy-index.yaml
```

Regenerate atomic skills from catalog and taxonomy inputs:

```powershell
python scripts/build_skills.py
```

Regenerate professional skillsets:

```powershell
python scripts/build_skillsets.py
```

Regenerate per-skill host metadata:

```powershell
python scripts/generate_openai_metadata.py
```

Regenerate root AgentSkills-style routing templates:

```powershell
python scripts/generate_agent_routing_templates.py
```

Run the full local gate:

```powershell
.\scripts\validate-all.ps1
```

Preview public skill packaging:

```powershell
.\scripts\publish_skill_repository.ps1 -DryRun
```

## Editing generated artifacts

Prefer changing generator inputs or generator scripts instead of hand-editing
generated skills, professional wrappers, metadata, or routing files. Hand
edits can be overwritten during regeneration. Review the generated diff and
run validation after each regeneration step.

## Evidence and test discipline

Use fictional records in fixtures and examples. Treat scenario files as
specifications until outputs have been captured and scored. Keep source
records dated and limitation-aware; access date alone does not prove legal
currentness or site applicability.

## Release checks

Before release tagging, run the full validation gate, preview GitHub skill
packaging, install each professional skillset from the public release ref in a
fresh destination project, and update `docs/development/CC-39-final-audit.md`
with exact evidence and known limitations.
