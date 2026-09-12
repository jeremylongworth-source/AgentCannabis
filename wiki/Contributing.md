# Contributing

Contributions are welcome when they improve a bounded review workflow without
weakening the taxonomy, source, safety, or validation contracts.

## Before editing

Read `CONTRIBUTING.md`, `AGENTS.md`, `ROADMAP.md`,
`docs/architecture/scope-boundaries.md`,
`docs/architecture/prohibited-capabilities.md`,
`docs/standards/skill-authoring-standard.md`, and
`docs/standards/regulatory-source-standard.md`.

Declare the affected wave, files, source research, validation, and known
limits before changing a skill or generated artifact.

## Contribution rules

- Preserve the frozen 233-skill Master Taxonomy v1.0 unless a future version
  explicitly changes it.
- Keep every installable skill self-contained inside its own folder.
- Do not add unsafe operational cannabis instructions.
- Do not add legal, engineering, QAP, lot-release, filing, pesticide, CTLS,
  CRA, hazardous-process, or professional-approval authority.
- Use fictional records in tests and examples.
- Keep source records targeted, dated, and limitation-aware.
- Do not include secrets, real regulated-site records, credentials,
  signatures, or confidential commercial data.
- Change generator inputs or scripts when an artifact is generated; do not rely
  on hand-edits that regeneration will erase.

## Validation before a pull request

```powershell
.\scripts\validate-all.ps1
.\scripts\publish_skill_repository.ps1 -DryRun
```

A good pull request states what changed, which skills or docs are affected,
which safety boundary was considered, what validation was run, and whether
source-currentness or applicability changed.

## Review expectations

Reviewers should be able to trace each readiness claim to a file, command
output, or evaluation report. Installation success proves package availability;
it does not prove legal correctness, current site applicability, or future
model behavior.
