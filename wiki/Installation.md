# Installation

AgentCannabis publishes portable Agent Skills packages. You can install a
professional role package or an atomic skill with GitHub CLI, or load the
repository folders directly in a local agent host.

Use a release tag for a reproducible installation. The current documented
release is `v1.0.5`.

## Prerequisites

- Git and a destination Git project for project-scoped installs.
- GitHub CLI with `gh skill` support.
- PowerShell 5.1 or newer and Python 3.11 or newer for repository helpers and
  validation.

Check the installed command surface before choosing a host:

```powershell
gh --version
gh skill install --help
```

## Install a professional skillset with GitHub CLI

Run these commands from the destination project. The path is an exact folder
inside the public repository, which avoids a full repository skill scan:

```powershell
gh skill preview jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist@v1.0.5
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist --agent github-copilot --scope project --pin v1.0.5
```

The example targets GitHub Copilot. `gh skill install` supports other hosts;
choose an `--agent` value supported by your installed GitHub CLI and follow the
host's discovery instructions. Project scope places the package in the
host's project skill location. Use `--scope user` when you deliberately want
user-wide availability.

Do not combine an inline `@VERSION` with `--pin`. Put the ref in one place:

```powershell
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist@v1.0.5 --agent github-copilot --scope project
```

For development content, replace the tag with `@main`; a branch is mutable
and should not be used when reproducibility matters.

## Install an atomic skill

Choose a folder name from the [Taxonomy](Taxonomy) page or `skills/` directory:

```powershell
gh skill preview jeremylongworth-source/AgentCannabis skills/build-crop-monitoring-plan@v1.0.5
gh skill install jeremylongworth-source/AgentCannabis skills/build-crop-monitoring-plan --agent github-copilot --scope project --pin v1.0.5
```

Atomic skills are useful for narrow tasks. Start with a professional wrapper
when a request spans several families or needs role-level routing.

## Install from a local clone

From an AgentCannabis checkout, the manifest helper validates the selected
professional manifest and installs the self-contained wrapper into another Git
project:

```powershell
.\scripts\install_skillset.ps1 -Skillset cannabis-compliance-specialist -ProjectPath D:\MyProject -Ref v1.0.5 -Pin -WhatIf
.\scripts\install_skillset.ps1 -Skillset cannabis-compliance-specialist -ProjectPath D:\MyProject -Ref v1.0.5 -Pin
```

Add `-IncludeMembers` only when the destination host should discover every
atomic member separately. The default wrapper includes its member index and
references inside one installation folder.

## Use the portable routing templates

For a local agent host that reads project instructions:

1. Start with `agents/AGENTS.base.md`, `agents/AGENTS.full.md`, or the focused
   `agents/AGENTS.<skillset-name>.md` file.
2. Load the selected `skills/<name>/SKILL.md`.
3. Load referenced files only when needed for the task.
4. Keep evidence gaps, source-currentness limits, and human approval gates in
   the output.

See [Agent Routing](Agent-Routing) and [Architecture](Architecture) for the
package and routing model.

## Confirm availability

Use fictional records after installation:

```text
Use $cannabis-compliance-specialist to identify missing licence, role,
inventory, quality, and source-currentness evidence in a fictional site
package. Do not approve, sign, submit, release, or operate anything.
```

The skill should identify the selected workflows, preserve missing evidence,
state source limits, and route regulated or hazardous decisions to the
responsible human or qualified professional.

## Troubleshooting

- If `gh skill` is unavailable, update GitHub CLI or use the portable local
  Agent Skills path.
- If the package is not visible, confirm the destination project, exact folder,
  supported skill location, and host reload behavior.
- If a skill already exists, preview the new version and inspect local changes
  before replacing it.
- If a local validation command fails, run
  `python scripts/validate_repository.py --stage full` to isolate the first
  structural error.
- If publishing from a Windows checkout reports a false Git ownership warning,
  use the repository's scoped wrapper rather than changing global Git config.

## Publishing validation

From an AgentCannabis clone, preview the package without publishing:

```powershell
.\scripts\publish_skill_repository.ps1 -DryRun
```

The wrapper scopes Git's `safe.directory` setting to the `gh skill publish`
process when required. It does not change persistent Git configuration.
