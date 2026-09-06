# AgentCannabis Professional Skillsets

Status: `READY`

Professional skillsets compose existing atomic AgentCannabis skills into role-level systems. They are portable Agent Skills packages under `skills/<skillset-name>/` with matching manifests in `skillsets/<skillset-name>.json` and routing templates in `agents/AGENTS.<skillset-name>.md`.

They do not duplicate all member procedures in the manifest and do not create legal, QAP, lot-release, engineering, pesticide, CTLS, CRA, hazardous-process, or site-specific compliance authority.

## Required Roles

- `cultivation-technician`
- `cultivation-manager-support`
- `master-grower-support`
- `plant-health-specialist`
- `controlled-environment-cultivation-specialist`
- `post-harvest-technician`
- `drying-curing-specialist`
- `post-harvest-manager`
- `cannabis-processing-technician`
- `processing-manager-support`
- `preventive-controls-specialist`
- `quality-control-specialist`
- `qap-support`
- `cannabis-quality-systems-specialist`
- `cannabis-compliance-specialist`
- `ctls-inventory-specialist`
- `cannabis-production-manager`
- `cannabis-operations-manager`

## Composition Gate

- Professional skillsets compose existing atomic skills from `skills/`.
- Role packages must not add hidden procedures, hidden approvals, or new regulated conclusions.
- Role outputs must preserve evidence boundaries, source gaps, owner handoffs, escalation conditions, and qualified-review requirements.
- GitHub Copilot installation is a supported distribution path, not the only intended use.
- Root `agents/AGENTS.*.md` files provide AgentSkills-style routing for Codex and other local-agent hosts.

## Validation

Run:

```powershell
.\scripts\validate-all.ps1
gh skill publish D:\AgentCannabis --dry-run
```
