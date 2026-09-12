# Peer consistency review

Run date: 2026-09-06. Scope: compare AgentCannabis against local peer repositories `D:\CodexProject\AgentSkills`, `D:\ChefSkills`, `D:\AgentInvestigate`, and `D:\AgentLogistics`.

## Findings before changes

AgentCannabis was complete against its original roadmap and GitHub Copilot distribution requirement, but it read more narrowly than AgentSkills and the peer repositories:

- README framed the project as a "GitHub Copilot skill repository" rather than a portable AI Agent Skills repository.
- Skill folders lacked `agents/openai.yaml`, while AgentSkills, ChefSkills, and representative peer packages include host-facing metadata.
- AgentCannabis had no root `agents/AGENTS.*.md` routing templates, while AgentSkills and ChefSkills expose skillset routing outside Copilot install mechanics.
- AgentCannabis had no peer-style `scripts/validate-all.ps1` wrapper.
- AgentCannabis had no GitHub validation workflow, source metadata workflow, pull request template, or issue templates.
- AgentCannabis lacked `.gitattributes`, while the peer repos pin text files to LF and PowerShell scripts to CRLF.
- `skillsets/` had manifests but no README explaining professional composition boundaries.

## Changes made

- Reframed README and wiki wording around portable AI Agent Skills, with GitHub Copilot documented as one supported distribution path.
- Added `agents/openai.yaml` metadata to all 251 installable skill folders.
- Added root `agents/AGENTS.base.md`, `agents/AGENTS.full.md`, and one `agents/AGENTS.<skillset>.md` routing template for each of the 18 professional skillsets.
- Added `scripts/generate_agent_routing_templates.py` for deterministic root routing-template regeneration from existing skillset manifests.
- Extended `scripts/validate_repository.py` to require `agents/openai.yaml`, validate the default prompt names each skill, and require AgentSkills-style root routing templates.
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

.\scripts\publish_skill_repository.ps1 -DryRun
Dry run complete

gh skill install jeremylongworth-source/AgentCannabis skills/<professional-skillset> --agent github-copilot --scope project --pin v1.0.2
18 professional skillsets installed from the public tag
```

Direct `gh skill publish --dry-run` can emit a false Windows ownership warning when the checkout owner differs from the interactive user. Use `scripts/publish_skill_repository.ps1 -DryRun` to scope Git's `safe.directory` override to the publish process. Public tagged installs pass for every professional skillset.

## Remaining difference from peers

AgentCannabis intentionally keeps JSON professional skillset manifests because the existing generator and installer validate `skillsets/<name>.json`. AgentSkills uses YAML manifests with `agents_file` links, ChefSkills uses a small YAML bundle set, AgentInvestigate uses an aggregate JSON manifest, and AgentLogistics uses directory-based role packages. AgentCannabis now matches the portable routing behavior through root `agents/AGENTS.*.md` templates without breaking its verified public install surface.

AgentCannabis also keeps generated atomic skills highly regular. That is acceptable for v1.0 because the source taxonomy is broad, the behavior boundaries are centralized, and evaluation reports cover reference, integrated, and adversarial behavior. Future releases should strengthen selected high-use skills with deeper task-specific references based on observed usage.
