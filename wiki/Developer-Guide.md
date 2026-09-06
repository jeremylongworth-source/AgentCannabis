# Developer Guide

This page is for maintainers changing AgentCannabis locally.

## Common commands

Import the supplied taxonomy source:

```powershell
python scripts/import_taxonomy.py --source "C:\Users\jerem\Desktop\Taxonomy Canadian Cannabis Skill Repositor.txt" --output docs/architecture/taxonomy-index.yaml
```

Regenerate atomic skills from catalog and taxonomy inputs:

```powershell
python scripts/build_skills.py
```

Regenerate professional skillsets:

```powershell
python scripts/build_skillsets.py
```

Regenerate per-skill OpenAI metadata:

```powershell
python scripts/generate_openai_metadata.py
```

Regenerate root AgentSkills-style routing templates:

```powershell
python scripts/generate_agent_routing_templates.py
```

Run the full local gate:

```powershell
.\scriptsalidate-all.ps1
```

## Editing generated artifacts

Prefer changing generator inputs or generator scripts instead of hand-editing generated skills, professional wrappers, metadata, or routing files. Hand edits can be overwritten during regeneration.

## Release checks

Before release tagging, run validation, preview GitHub skill packaging, install each professional skillset from the public ref in a fresh Git project, and update the final audit with exact evidence.
