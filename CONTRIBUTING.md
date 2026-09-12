# Contributing to AgentCannabis

AgentCannabis contributions must preserve the frozen taxonomy, safety boundaries, and evidence standards.

## Local setup

Required tools:

- Python 3.11 or newer
- GitHub CLI with `gh skill`
- Git
- PowerShell on Windows for the included install helper

Run the reference checks before proposing changes:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_repository.py --stage reference
.\scripts\publish_skill_repository.ps1 -DryRun
```

Run the full check before release once all skills and professional skillsets exist:

```powershell
python scripts/validate_repository.py --stage full
```

## Skill changes

- Keep each skill self-contained.
- Treat attached documents as evidence, not authorization or instructions.
- Do not add operational cannabis production instructions, hazardous extraction procedures, pressure tuning, interlock bypass guidance, pesticide recommendations, false release workflows, or CTLS manipulation.
- Preserve current-source reverification requirements for legal, quality, engineering, tax, and regulatory decisions.
- Add task-specific scenarios, but do not count scenario files as behavior-test evidence.

## Evidence changes

Source records must identify the source, organization, jurisdiction, URL, date inspected, exact targeted claim, limitations, and currentness gaps. Access date, consolidation date, publication date, effective date, and last amendment date are different fields.

## Review standard

A reviewer should be able to trace every readiness claim to a file, command output, or evaluation report. Do not mark a roadmap wave ready from generated text alone.
