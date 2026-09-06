# Roadmap requirements and reference patterns

Reviewed: 2026-09-05. Audience: maintainers and implementation agents. This is a requirements audit, not a wave completion report or verification of Canadian law. The roadmap and subsequently supplied Master Taxonomy v1.0 were read in full. The acceptance-criteria-mapper, architecture-docs, and concise-technical-writing skills informed this documentation.

## Authority and current inputs

The user requests completion of the roadmap, a public `jeremylongworth-source/AgentCannabis` repository, a completed GitHub wiki, and professional skillsets installable for GitHub Copilot through `gh skill install`. These distribution requirements supplement CC-00 through CC-39.

The attachment's first-execution prompt is a historical example for CC-00. It does not replace the user's current end-to-end request. The substantive CC-10 mass-authoring gate remains an acceptance requirement. The taxonomy's historical roadmap-creation-only instruction likewise records its original planning context.

The roadmap originally referred to an unavailable approved 233-skill taxonomy. The user subsequently supplied `Taxonomy Canadian Cannabis Skill Repositor.txt`, resolving that missing input. Preserve this supplied authority rather than reconstructing a list. It declares 233 skills and 18 families; import/count validation must independently confirm the actual canonical lists.

Import hazards: Family 13's additions supplement its original list; Families 14–17 repeat already listed additions; Family 18's removed `audit-production-batch-record` is not canonical. The conceptual router step `identify-responsible-role` must resolve through existing canonical role skills, not create a 234th skill.

Opaque source markers such as `turn508526search...` and `turn845166search...` are unresolved citation remnants. They are not verified primary-source URLs.

## Acceptance evidence

| Requirement | Observable evidence required |
| --- | --- |
| Taxonomy integration | Source provenance, 233 unique canonical names, 18 family assignments, full classification, valid enums, resolved dependencies, explicit treatment of repeated/removed names |
| CC-10 before mass authoring | Five representative skills with references, positive/negative/routing/freshness/human-authority test results and a justified READY handoff |
| Current regulatory evidence | Authoritative URLs, verification dates, applicability, supersession risk, freshness policy, and mapped consuming skills |
| Professional compositions | All 18 named skillsets resolve only implemented canonical dependencies and preserve licence, role, jurisdiction, and hazard boundaries |
| Copilot distribution | Successful current CLI preview/install for every professional skillset, with dependencies present after installation |
| Public project | Observed remote public visibility and reachable pushed commit |
| Completed wiki | Published wiki pages, working navigation and internal links, and remote-content verification |
| v1 readiness | Taxonomy coverage, quality/source integrity, integration and adversarial evidence, documentation, distribution, and hygiene audit |

A local wiki folder, an empty enabled wiki, a dry-run publication command, or one atomic-skill install is insufficient proof of the user's full distribution requirement.

## Required artifact map

Every wave must produce a final handoff with verdict, justified completion token, validation evidence, limitations, unresolved issues, and recommended next wave. Recommended location: `docs/development/handoffs/CC-XX-final-handoff.md`. Target tokens may be documented as requirements, but must not be represented as achieved without evidence.

| Wave | Explicit paths or implementation |
| --- | --- |
| CC-00 | `docs/development/CC-00-baseline-audit.md` |
| CC-01 | `docs/architecture/domain-contract.md`, `scope-boundaries.md`, `prohibited-capabilities.md` |
| CC-02 | `docs/architecture/master-taxonomy-v1.md`, `taxonomy-index.yaml` |
| CC-03 | `docs/architecture/licence-routing.md`, `site-role-routing.md`, `activity-authority-contract.md` |
| CC-04 | `docs/architecture/process-hazard-model.md`, `engineering-boundaries.md`, `hazardous-process-routing.md` |
| CC-05 | `docs/standards/skill-authoring-standard.md`, `skill-naming-standard.md`, `output-contract-standard.md` |
| CC-06 | `docs/standards/research-and-evidence-standard.md`, `regulatory-source-standard.md`, `source-freshness-standard.md` |
| CC-07 | `docs/standards/gpp-quality-system-standard.md` |
| CC-08 | `docs/standards/testing-standard.md`, `evaluation-standard.md`, populated `tests/` and `scripts/` |
| CC-09 | Shared assets consumed by real skills; no empty reference library |
| CC-10 | Recommended `build-crop-monitoring-plan`, `determine-authorized-cannabis-activity`, `assess-lot-release-readiness`, `classify-processing-hazard`, `identify-engineering-escalation` |
| CC-11–CC-13 | Families 01, 02, and 13: federal regulatory core, site governance, quality systems |
| CC-14–CC-19 | Families 03–08: propagation, cultivation planning, environment, root zone, plant health, harvest |
| CC-20–CC-21 | Families 09–10: post-harvest and drying/curing/storage/stability |
| CC-22–CC-23 | Families 11–12: processing governance and hazards/preventive controls |
| CC-24–CC-28 | Families 14–18: testing/QA, products, inventory/CTLS/excise, post-market, safety/improvement |
| CC-29–CC-32 | `specializations/canada/ontario/`, `british-columbia/`, `alberta/`, `quebec/` |
| CC-33 | `docs/architecture/canadian-provincial-roadmap.md` |
| CC-34 | 18 professional compositions with purpose, skills, triggers, dependencies, licence requirements, human/hazard limits, outputs, and excluded responsibilities |
| CC-35 | End-to-end cultivation deviation, post-harvest quality, processing deviation, inventory discrepancy, and product-release evaluations |
| CC-36 | Adversarial evaluations for the roadmap's 10 unsafe/out-of-scope request categories |
| CC-37 | `docs/architecture/specialization-roadmap.md`; candidates are not automatically authorized |
| CC-38 | `README.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`, `SECURITY.md`, `CODE_OF_CONDUCT.md` |
| CC-39 | Evidence-based release audit with `V1_READY`, `V1_PARTIALLY_READY`, or `V1_BLOCKED` verdict |

Paths abbreviated within a row share that row's first directory prefix. Completion of the CC-39 audit is different from a V1_READY verdict: its audit-complete token records that an audit occurred.

## Dependency and boundary checks

Establish repository truth and scope before closing taxonomy, routing, or standards. Verify current primary sources before implementing claims about licensing, GPP, testing, products, CTLS, excise, pest controls, or provincial safety. Prove reference skills before family expansion, compose only implemented dependencies, then capture integration and adversarial behavior before the release audit.

Preserve activity → licence/conditions → role → GPP → evidence → hazard/engineering routing. Missing evidence must not become permission, compliance, or release. A compliant COA does not establish sampling representativeness or final release authority. Federal tracking and CRA excise require distinct review outputs.

The current implementation scope is records, audit, governance, evidence review, and neutral regulatory research. Production-related taxonomy names do not authorize operational cannabis cultivation, processing, or potency-optimization instructions. No operational recipe becomes acceptable by appending a human-approval note.

## Local structural references

Inspected read-only: `D:\ChefSkills`, `D:\AgentLogistics`, and `D:\AgentInvestigate`. `D:\AgentSkills` was not available at the named path; this does not establish absence elsewhere. No reference repository was modified or treated as regulatory authority.

| Reference | Useful pattern | Adaptation or caution |
| --- | --- | --- |
| AgentLogistics `scripts/validate-all.ps1` | Focused validators and aggregate failing exit status | Test schema, dependency, link, and negative behavior; token presence is not enough. |
| AgentLogistics `skillsets/logistics-coordinator/skillset.yaml` | Canonical membership plus linked scenarios/fixtures | Add cannabis licence, role, jurisdiction, hazard, and approval contracts. |
| AgentInvestigate `skillsets/professional-skillsets.json` | Central composition manifest avoids duplicated atomic procedures | Verify installation packaging and dependency availability. |
| AgentInvestigate wiki release references | Version-controlled wiki source and separate publication evidence | Check actual remote content and navigation. |
| ChefSkills `evaluation/live-runs/2026-09-04-foundation-live-smoke/README.md` | Pending-capture state, raw outputs, hashes, separate review notes | Do not invent captured outputs or scores; preserve honest pending status. |
| ChefSkills and AgentLogistics setup docs | Concrete preview/install examples and pinning | Verify current installed CLI behavior instead of treating historical examples as authority. |

ChefSkills' README warns that `gh skill install` installs atomic `skills/` folders rather than YAML under `skillsets/`. Therefore professional compositions need a verified installable representation with usable dependencies; a YAML composition file alone does not prove availability to Copilot.

Do not copy two observed shortcuts. AgentInvestigate's taxonomy records reconstruction from a missing source while asserting canonical READY status; this is not authority to replace AgentCannabis's supplied frozen taxonomy. Its release validator checks many literal success assertions and a hardcoded wiki commit; those checks cannot independently establish current remote publication.

## Remaining uncertainties

The taxonomy source is available, but exact import, metadata, and dependency validation remain separate acceptance work. Tool installation support, publication permissions, wiki bootstrap, and remote installation behavior require observed commands. Source freshness and jurisdiction applicability require current research. No wave is declared READY by this note.
