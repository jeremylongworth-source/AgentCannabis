# Installation

Install a professional skillset as one self-contained Copilot skill. Each wrapper includes its member references, so it works without installing sibling atomic skills.

Use Git and a GitHub CLI version with `gh skill` support. The examples are compatible with **GitHub CLI 2.92.0**. From the Git project where you want Copilot to use AgentCannabis:

```powershell
gh --version
gh skill preview jeremylongworth-source/AgentCannabis cultivation-technician@main
gh skill install jeremylongworth-source/AgentCannabis skills/cultivation-technician@main --agent github-copilot --scope project
```

Choose another professional role from the [skillset manifests](https://github.com/jeremylongworth-source/AgentCannabis/tree/main/skillsets). `main` is the moving development branch. For a reviewed release, replace `TAG` below with a published tag or commit SHA:

```powershell
gh skill preview jeremylongworth-source/AgentCannabis cultivation-technician@TAG
gh skill install jeremylongworth-source/AgentCannabis skills/cultivation-technician --agent github-copilot --scope project --pin TAG
```

Do not combine an inline `@VERSION` with `--pin`. Project installs use `.agents/skills` in GitHub CLI 2.92.0. This CLI version has no install `--all` flag; install individual skills or use the manifest helper. [GitHub CLI install reference](https://cli.github.com/manual/gh_skill_install)

## Optional manifest helper

From an AgentCannabis clone, preview installation into an existing destination Git project:

```powershell
./scripts/install_skillset.ps1 -Skillset cultivation-technician -ProjectPath D:/MyProject -Ref main -WhatIf
```

Replace the destination path and remove `-WhatIf` to install. By default the helper installs the wrapper alone. Add `-IncludeMembers` to install its atomic skills as separate entries too. Use `-Ref TAG -Pin` with a local checkout of the matching release for a pinned release install.

The helper validates the local manifest and declared skill paths before invoking individual project-scoped `gh skill install` calls. It does not force overwrites or change global Git settings. A failed member installation stops the sequence; any earlier successful installs remain in place.

## Confirm availability

In Copilot CLI, open the destination project and run:

```text
/skills reload
/skills list
/skills info cultivation-technician
```

Test with fictional records and a request for a draft checklist. Confirm Copilot loads the wrapper, reads its bundled references, and retains its human review and hazard boundaries. Installation does not grant professional authority or permission to perform regulated work. [Copilot CLI skills documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)

See the [complete installation guide](https://github.com/jeremylongworth-source/AgentCannabis/blob/main/docs/guides/copilot-installation.md) for atomic skills, version handling, updates, and troubleshooting. Preview each new version before adoption and review changes to its regulatory sources and boundaries.
