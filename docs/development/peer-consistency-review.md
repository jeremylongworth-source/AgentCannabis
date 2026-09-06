# Peer consistency review

Run date: 2026-09-06. Scope: compare AgentCannabis against local peer repositories `ChefSkills`, `AgentInvestigate`, and `AgentLogistics`, plus the installed AgentSkills conventions available in the local skill system. A local `AgentSkills` repository checkout was not found under `D:\` or `C:\Users\jerem` during this pass.

## Findings before changes

AgentCannabis was complete against its original roadmap and GitHub Copilot distribution requirement, but it read more narrowly than the peer repositories:

- README framed the project as a "GitHub Copilot skill repository" rather than a portable AI Agent Skills repository.
- Skill folders lacked `agents/openai.yaml`, while representative ChefSkills and AgentLogistics packages included that host-facing metadata.
- AgentCannabis had no peer-style `scripts/validate-all.ps1` wrapper.
- AgentCannabis had no GitHub validation workflow, source metadata workflow, pull request template, or issue templates.
- AgentCannabis lacked `.gitattributes`, while the peer repos pin text files to LF and PowerShell scripts to CRLF.
- `skillsets/` had manifests but no README explaining professional composition boundaries.

## Changes made

- Reframed README and wiki wording around portable AI Agent Skills, with GitHub Copilot documented as one supported distribution path.
- Added `agents/openai.yaml` metadata to all 251 installable skill folders.
- Extended `scripts/validate_repository.py` to require `agents/openai.yaml` and validate the default prompt names each skill.
- Added `scripts/generate_openai_metadata.py` for deterministic metadata regeneration.
- Added `scripts/validate-all.ps1` as the peer-style validation entrypoint.
- Added `scripts/validate-source-links.py` for deterministic source registry URL and limitation checks.
- Added `.gitattributes` matching the peer line-ending convention.
- Added `.github/workflows/validate.yml` and `.github/workflows/source-links.yml`.
- Added `.github/pull_request_template.md` and issue templates for skill requests, source issues, and evaluation gaps.
- Added `skillsets/README.md` describing the 18 professional role compositions and their boundaries.
- Added `docs/setup/agent-skills.md` and `docs/setup/README.md` for non-Copilot host usage.

## Validation

The following checks passed after the changes:

```text
.\scripts\validate-all.ps1
All AgentCannabis validation checks passed.

quick_validate.py across 251 skill folders
PASS

gh skill publish D:\AgentCannabis --dry-run
Dry run complete
```

`gh skill publish --dry-run` still warns that no active tag protection rulesets exist. That is a GitHub repository governance improvement, not a local package or installability failure.

## Remaining difference from peers

AgentCannabis intentionally keeps a flatter `skills/<name>/` layout, while AgentLogistics uses domain-subfolders and AgentInvestigate uses roadmap-generated family packaging. The flatter layout matches the already verified `gh skill install` commands for this repository and avoids breaking the public install surface.

AgentCannabis also keeps generated atomic skills highly regular. That is acceptable for v1.0 because the source taxonomy is broad, the behavior boundaries are centralized, and evaluation reports cover reference, integrated, and adversarial behavior. Future releases should strengthen selected high-use skills with deeper task-specific references based on observed usage.
