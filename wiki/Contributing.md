# Contributing

Contributions are welcome when they preserve the project boundaries and validation gate.

## Before editing

Read `CONTRIBUTING.md`, `AGENTS.md`, `docs/architecture/scope-boundaries.md`, `docs/architecture/prohibited-capabilities.md`, `docs/standards/skill-authoring-standard.md`, and `docs/standards/regulatory-source-standard.md`.

## Contribution rules

- Preserve the frozen 233-skill Master Taxonomy v1.0 unless a future version explicitly changes it.
- Keep every skill self-contained inside its own folder.
- Do not add unsafe operational cannabis instructions.
- Do not add legal, engineering, QAP, lot-release, filing, pesticide, CTLS, CRA, or professional approval authority.
- Use fictional records in tests and examples.
- Keep source records targeted, dated, and limitation-aware.
- Do not include secrets, real regulated-site records, credentials, signatures, or confidential commercial data.

## Validation before a pull request

```powershell
.\scriptsalidate-all.ps1
gh skill publish . --dry-run
```

A good pull request states what changed, which skills or docs are affected, what safety boundary was considered, what validation was run, and whether source-currentness or applicability changed.
