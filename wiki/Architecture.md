# Architecture

AgentCannabis separates domain authority, reusable skills, role composition,
and host distribution so a package can be installed without granting the
agent permission to make a regulated decision.

## Layers

```text
Master Taxonomy v1.0
        |
        v
233 atomic skill packages  <--- source records, contracts, scenarios
        |
        v
18 professional skillset wrappers  <--- member index and bundled references
        |
        +--> root agents/ routing templates for local hosts
        +--> gh skill install for supported Agent Skills hosts
```

### Taxonomy

The Master Taxonomy v1.0 defines 233 unique atomic skills across 18 families.
It is frozen for the v1 release. Validators enforce the count, unique names,
family counts, metadata fields, and documented aliases.

### Atomic packages

Every installable skill under `skills/<name>/` is self-contained and includes
its main `SKILL.md`, host metadata where applicable, a review contract, source
records, and scenario specifications. References are loaded progressively so a
host can start with the smallest useful package.

### Professional wrappers

Each professional package composes existing atomic skills without duplicating
their procedures. Its member index records the included workflows and its
bundled references keep the wrapper usable after a single install. A wrapper
does not add legal, QAP, lot-release, engineering, pesticide, CTLS, CRA,
hazardous-process, or site-specific authority.

### Routing

The root `agents/` directory contains generated AgentSkills-style templates:

- `AGENTS.base.md` for shared boundaries and review behavior;
- `AGENTS.full.md` for all professional packages; and
- one `AGENTS.<skillset-name>.md` file for each focused role package.

These templates help local hosts route broad requests to a role package and
narrow requests to an atomic skill. They are generated from the manifests and
wrapper text; use the generator instead of editing generated routing files by
hand.

### Distribution

GitHub CLI can preview and install a release-tagged skill folder. The example
below targets GitHub Copilot, while the CLI supports other Agent Skills hosts:

```powershell
gh skill preview jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist@v1.0.5
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist --agent github-copilot --scope project --pin v1.0.5
```

## Review model

The architecture keeps four questions separate:

1. What evidence is present?
2. What source or applicability limits remain?
3. What risk or authority route applies?
4. Which authorized human or qualified professional must decide or act?

Agent output remains review assistance. A complete checklist, draft, or
evidence package is never itself authorization to sign, submit, release,
destroy, recall, file, operate equipment, or change regulated records.
