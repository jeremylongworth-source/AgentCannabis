# Install AgentCannabis for GitHub Copilot

Install one professional skillset to give Copilot its role-specific workflow and bundled member references. AgentCannabis skills are portable Agent Skills; this page documents the GitHub Copilot distribution path. Each skillset is a self-contained skill under `skills/<skillset-name>/`; its JSON manifest in `skillsets/` describes the composition. Atomic skills can also be installed separately.

These instructions use `cultivation-technician` as an example. Choose another name from the [skillset manifests](../../skillsets/). Development examples select `main` explicitly. For a release, replace `TAG` with an actual tag from [GitHub Releases](https://github.com/jeremylongworth-source/AgentCannabis/releases).

## Requirements

- Git and GitHub CLI with `gh skill` support. Commands below are compatible with GitHub CLI **2.92.0**.
- GitHub access through your existing CLI authentication and network connection.
- A destination Git project where you want Copilot to use the skills.
- A Copilot host that supports Agent Skills.

Check the installed CLI before continuing:

```powershell
gh --version
gh skill install --help
gh auth status
```

`gh skill` remains a preview feature. The online manual can describe flags absent from an older installed CLI. Version 2.92.0 has no `gh skill install --all` or `gh skill list`; this guide uses individual installs. [GitHub CLI install manual](https://cli.github.com/manual/gh_skill_install)

## Preview and install one skillset

Run these commands from your **destination project**:

```powershell
gh skill preview jeremylongworth-source/AgentCannabis cultivation-technician@main
gh skill install jeremylongworth-source/AgentCannabis skills/cultivation-technician@main --agent github-copilot --scope project
```

Review the wrapper and its references before use. The wrapper carries its member workflows inside its own directory, so this single install provides the professional skillset. It does not require sibling skill directories or a repository clone at runtime.

GitHub CLI 2.92.0 places project Copilot skills in `.agents/skills`. Copilot also supports `.github/skills` and `.claude/skills` for project discovery. Keep only the copies you intend the host to load. [Copilot skill locations](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

`main` moves as development proceeds. For a reviewed release, use a tag or commit SHA and `--pin`:

```powershell
gh skill preview jeremylongworth-source/AgentCannabis cultivation-technician@TAG
gh skill install jeremylongworth-source/AgentCannabis skills/cultivation-technician --agent github-copilot --scope project --pin TAG
```

Do not combine `@VERSION` and `--pin`. Pinning a release or commit lets you review a new version before reinstalling it. A branch name is not an immutable version.

## Use the manifest installer

With a local clone of AgentCannabis, the PowerShell helper validates `skillsets/<name>.json`, its matching name, its unique `included_skills`, and the corresponding repository skill files. It accepts skill names, not arbitrary manifest paths. Preview its plan first:

```powershell
./scripts/install_skillset.ps1 -Skillset cultivation-technician -ProjectPath D:/MyProject -Ref main -WhatIf
```

Replace `D:/MyProject` with an existing destination Git project, then run without `-WhatIf`:

```powershell
./scripts/install_skillset.ps1 -Skillset cultivation-technician -ProjectPath D:/MyProject -Ref main
```

The default installs only the self-contained wrapper. To make its atomic member skills independently discoverable as well:

```powershell
./scripts/install_skillset.ps1 -Skillset cultivation-technician -ProjectPath D:/MyProject -Ref main -IncludeMembers
```

For a release, use a local checkout of that same release so its manifest agrees with the remote files:

```powershell
./scripts/install_skillset.ps1 -Skillset cultivation-technician -ProjectPath D:/MyProject -Ref TAG -Pin
```

The helper invokes one `gh skill install` per selected skill at project scope. It does not change global Git settings, request extra authentication scopes, force overwrite existing skills, or change your PowerShell execution policy. `-WhatIf` reads local files and checks the destination Git worktree but performs no installation. If an install fails, it stops; earlier successful installs remain available for inspection.

## Install an atomic skill

Use the atomic folder name as the skill argument. Replace `ATOMIC-SKILL` with a name from the [canonical skills directory](../../skills/):

```powershell
gh skill preview jeremylongworth-source/AgentCannabis ATOMIC-SKILL@main
gh skill install jeremylongworth-source/AgentCannabis skills/ATOMIC-SKILL@main --agent github-copilot --scope project
```

For personal availability across projects, the CLI also supports `--scope user`. Choose that scope explicitly; the repository helper always uses project scope.

## Confirm Copilot can use the skill

In a Copilot CLI session opened in the destination project:

```text
/skills reload
/skills list
/skills info cultivation-technician
```

Then try a document-only prompt with fictional records:

```text
Use /cultivation-technician to identify missing evidence in a fictional cultivation shift handoff. Ask for the jurisdiction, licence scope, approved site procedure, and records you need. Return a draft checklist for human review.
```

Confirm the host recognizes the skill, can read the bundled references, and keeps the output within the skill's human-authority and hazard boundaries. A successful file install establishes availability; it does not establish regulatory accuracy or permission to perform regulated work. [Copilot CLI skills and reload commands](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)

## Updates and troubleshooting

- **Command or flag missing:** inspect `gh skill --help` and your installed version. Do not assume a flag in the current online manual exists in 2.92.0.
- **Skill not found:** confirm the name, remote branch or tag, and that the selected version contains `skills/<name>/SKILL.md`. Use `@main` to test development content when a release predates it.
- **Authentication or network error:** check `gh auth status` and normal access to GitHub. Installation needs no cannabis-system credentials.
- **Git ownership error:** inspect the destination path and ownership. The helper will not add a global `safe.directory` exception.
- **Existing skill conflict:** inspect the installed version and local changes before deciding whether to replace it. The helper does not pass `--force`.
- **Copilot does not show the skill:** confirm the project root, supported skill directory, and exact uppercase `SKILL.md` filename, then reload the host.
- **Manifest validation fails:** use the repository's validated manifest and matching skill tree. A wrapper and its atomic member names must exist before the helper will run.

For a deliberate update, preview the new version and reinstall the selected skill at that version. `gh skill update` uses metadata recorded during installation; skills installed with `--pin` are skipped. Reassess regulatory source dates and the relevant workflow scenarios when upgrading. [GitHub skill management documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)

