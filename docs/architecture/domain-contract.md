# AgentCannabis domain contract

Status: CC-01 scope contract. This document defines repository behavior; it does not establish that later roadmap waves are implemented or validated.

## Purpose and audience

AgentCannabis provides professional records, audit, governance, evidence review, and neutral regulatory research support for Canadian commercial cannabis operations. Its intended users include authorized site personnel, quality teams, compliance personnel, and qualified reviewers. Skill names describe areas of support and confer no licence, certification, regulated role, or decision authority.

The project uses the supplied Canadian Cannabis Skill Repository Development Roadmap v0.1 and Master Taxonomy v1.0 as planning authorities. The taxonomy declares 233 atomic skills in 18 families. Import validation, metadata completion, skill implementation, and evaluation are separate work; the source document's READY labels do not prove repository readiness.

## Working definitions

These are repository scope definitions, not quotations or replacements for statutory definitions. Any legal classification requires current primary authority and the facts of the activity.

| Term | Meaning in this repository |
| --- | --- |
| Commercial cannabis | The regulated Canadian business context in which the repository reviews records, authority, evidence, and governance. It is not a consumer growing guide. |
| Cultivation | The domain covering crop records, monitoring evidence, provenance, capacity records, deviations, and governance review. |
| Post-harvest | The documented lifecycle of harvested material, including identity, intake, segregation, hold status, handling records, and quality investigation. |
| Drying | Review of recorded observations, measurement integrity, deviations, and evidence against an existing authorized facility procedure. |
| Curing | Review of recorded condition changes, quality observations, and procedure adherence after initial drying. |
| Processing | Classification and review of documented material transformations, authority, batch records, controls, changes, and deviations. |
| Refinement | A processing-domain term requiring activity and hazard classification; it is not an independent permission to operate equipment. |
| Quality assurance | Evidence preparation and quality-system review, with findings and unresolved gaps presented to the responsible human. |
| Testing | Review of sampling provenance, laboratory reports, specifications, uncertainty, and investigation records. |
| Traceability | Reconciliation of material identity, lot lineage, documented transformations, inventory movements, and reporting records. |
| Provincial overlay | A separately sourced jurisdiction module for applicable provincial or territorial requirements; never a substitute for the federal core. |
| Industrial hemp | A separate specialist boundary requiring its own scope and current legal classification. It is not automatically covered by the core. |

Cultivation, propagation, irrigation, drying, curing, and processing skills are limited to records, audit, governance, and evidence review. They must not generate operational cannabis production protocols, parameter recipes, potency improvements, or equipment instructions. Where a taxonomy verb says build or plan, the permitted output is an administrative monitoring, evidence, review, or governance artifact within this boundary.

## Architecture contract

The common control flow is activity classification → licence and conditions evidence → responsible role → quality-system evidence → hazard boundary → permitted review output → authorized human decision. Unknown information remains unknown throughout the route.

The federal core supplies shared regulatory research and authority-review structure. Family skills review bounded records or questions. Provincial modules add separately verified jurisdiction context. Professional skillsets compose canonical atomic skills without duplicating their procedures or overriding their boundaries. Source records connect claims to authority, applicability, and verification dates. Tests must distinguish structural checks from observed model behavior.

Every atomic skill must declare `family`, `tier`, `production_stage`, `jurisdiction`, `licence_dependency`, `responsible_role`, `regulatory_sensitivity`, `hazard_class`, `human_approval_required`, and `source_freshness`.

The roadmap's conceptual `identify-responsible-role` routing step is not a new atomic skill. Implement it through the canonical role skills, including `identify-required-site-roles` and `map-site-role-responsibilities`, with specific role review when applicable.

## Output and decision contract

Every substantive review separates supplied facts, verified sources, assumptions, missing evidence, findings, and actions requiring human review. It identifies the relevant jurisdiction, activity, licence evidence, responsible role, source verification date, and hazard boundary before presenting a conclusion dependent on them.

Outputs are draft review packages, evidence matrices, record discrepancies, question lists, monitoring-record structures, or administrative action plans. They never constitute QAP release, legal approval, regulatory submission, recall authorization, engineering approval, treatment authorization, or a change to live site controls.

Health Canada tracking preparation and CRA excise preparation remain distinct review streams even where they consume the same inventory records. No reconciliation may alter a source record to force a desired balance. Proposed corrections preserve the original, rationale, evidence, and authorized reviewer.

## Validation and review triggers

The contract is satisfied when authored skills have complete classification, resolve their canonical dependencies, preserve the output and decision boundaries, and pass relevant positive and negative scenarios. A source file, required phrase, or completion token alone is insufficient behavioral evidence.

Revisit this contract when an approved taxonomy change alters scope, current primary authority changes applicability, a new province is added, or evaluation reveals a boundary failure. Operational production procedures and specialist engineering are excluded from the current implementation even when a user describes a licensed site.

Open implementation work: complete the canonical taxonomy import; verify current regulatory sources; implement and evaluate the reference skill set; verify distribution packaging for all 18 professional skillsets. Their completion belongs to their respective waves.
