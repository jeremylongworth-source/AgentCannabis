# Skillsets

AgentCannabis publishes 18 professional skillsets. Each one is a self-contained wrapper under `skills/<skillset-name>/` with `SKILL.md`, `agents/openai.yaml`, `references/member-index.json`, `references/review-contract.md`, `references/sources.json`, and `references/scenarios.json`.

The JSON manifest under `skillsets/<skillset-name>.json` records the wrapper and included atomic member skills. The root routing file under `agents/AGENTS.<skillset-name>.md` helps local agent hosts route to the same role package without relying on Copilot.

## Install example

```powershell
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist --agent github-copilot --scope project --pin v1.0.4
```

## Professional role packages

| Skillset | Role | Focus | Member skills |
| --- | --- | --- | ---: |
| `cannabis-compliance-specialist` | cannabis compliance specialist | licence, role, product, inventory, reporting, complaints, safety, and audit evidence | 96 |
| `cannabis-operations-manager` | cannabis operations manager | end-to-end operational governance, compliance evidence, quality systems, inventory, post-market, and safety escalation | 233 |
| `cannabis-processing-technician` | cannabis processing technician | processing records, material intake, batch records, control measures, and deviation evidence | 63 |
| `cannabis-production-manager` | cannabis production manager | cross-stage production evidence, resource and deviation review, hazard escalation, records, and inventory impacts | 192 |
| `cannabis-quality-systems-specialist` | cannabis quality systems specialist | quality-system records, document control, training, CAPA, product quality, and post-market evidence | 84 |
| `controlled-environment-cultivation-specialist` | controlled-environment cultivation specialist | environmental monitoring evidence, trend review, sensor coverage, and qualified escalation | 47 |
| `ctls-inventory-specialist` | CTLS and inventory specialist | inventory reconciliation, CTLS readiness, loss/theft packages, destruction records, and discrepancy review | 39 |
| `cultivation-manager-support` | cultivation manager support | cultivation governance, capacity, deviations, people/role evidence, and safety escalation | 106 |
| `cultivation-technician` | cultivation technician | daily cultivation record review, monitoring gaps, crop observations, and escalation packages | 74 |
| `drying-curing-specialist` | drying and curing specialist | drying, curing, moisture, water activity, storage, and microbial-risk evidence review | 39 |
| `master-grower-support` | master grower support | crop-cycle evidence, plant health, environment records, and production variance review without optimization instructions | 84 |
| `plant-health-specialist` | plant-health specialist | plant-health evidence, pest/disease observations, treatment records, and quality trend handoff | 53 |
| `post-harvest-manager` | post-harvest manager | post-harvest workflow control, holds, quality packages, inventory, deviations, and complaints | 101 |
| `post-harvest-technician` | post-harvest technician | harvest identity, intake, handling, drying, curing, and quality-record gaps | 51 |
| `preventive-controls-specialist` | preventive controls specialist | hazard analysis, process controls, corrective actions, SOP execution, and safety escalation | 61 |
| `processing-manager-support` | processing manager support | processing authority, flow, yield reconciliation, hazard routing, GPP controls, and inventory review | 101 |
| `qap-support` | QAP support | QAP responsibility evidence, quality systems, product records, complaints, recalls, holds, and adverse-reaction packages | 74 |
| `quality-control-specialist` | quality control specialist | sampling, COA review, OOS evidence, specifications, product quality records, and release package support | 53 |

## Choosing a skillset

- Use technician packages for record-level review and escalation briefs.
- Use manager-support packages for cross-record coordination and responsible-human handoff.
- Use QAP, quality, compliance, CTLS, and operations packages for role-level review briefs across multiple families.
- If the task is narrow and the atomic skill is installed, use the atomic skill directly.
- If the task spans multiple domains, use the narrowest professional wrapper that covers the request.

Professional skillsets do not create legal, QAP, lot-release, engineering, pesticide, CTLS, CRA, hazardous-process, or site-specific compliance authority.
