---
name: identify-engineering-escalation
description: "Identify the qualified disciplines and jurisdiction evidence needed for an engineering-boundary review. Use for identify engineering escalation; review assistance only."
license: MIT
metadata:
  family: "12"
  tier: "SPECIALIST"
  production_stage: "hazard-review"
  jurisdiction: "PROVINCIAL_REQUIRED"
  licence_dependency: "Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns"
  responsible_role: "Qualified discipline professional and authorized site reviewer"
  regulatory_sensitivity: "HIGHLY_REGULATED"
  hazard_class: "ENGINEERING_BOUNDARY"
  human_approval_required: "true"
  source_freshness: "HIGH: reverify at decision time; repository review interval 30 days; access date is not legal currency"
  package_kind: "atomic"
---

# Identify engineering escalation

## Triggers

Identify the qualified disciplines and jurisdiction evidence needed for an engineering-boundary review.

## Non-triggers

No engineering calculations, equipment configuration, code-compliance certificate, ventilation sizing or professional sign-off.

## Inputs

Province/municipality, facility/activity scope, non-operational equipment identifiers, existing drawings/reports and approval references, reported concern and site safety owner.

## Assumptions and dependencies

Use [the review contract](references/review-contract.md). Do not assume absent licence, source, measurement or approval evidence. This package is self-contained; no other installed skill is required.

## Licence requirements and responsible role

Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns. Review owner: Qualified discipline professional and authorized site reviewer.

## Procedure

1. Identify whether the concern concerns pressure, fire/explosion, hazardous-location electrical, building occupancy, critical ventilation or another qualified discipline; record overlaps.
2. Require the actual province and project context before selecting regulatory research sources. Do not transfer Ontario assumptions to B.C., Alberta or Quebec.
3. Inventory existing professional documents by author, discipline, scope, revision and approval reference. Distinguish missing documents from an adverse engineering finding.
4. Draft questions for qualified professionals and the applicable authority having jurisdiction, with an explicit statement that neither compliance nor safe operation has been certified.

## Evidence and source requirements

Retain record IDs, versions, dates, units/basis and provenance. Consult relevant entries in [the source snapshot](references/sources.json), then reverify the specific current primary authority and applicability. Missing or stale evidence remains an explicit gap.

## Hazard behavior and human approval

No engineering calculations, equipment configuration, code-compliance certificate, ventilation sizing or professional sign-off. Authorized humans retain release, filing, recall and engineering decisions.

## Outputs and limitations

Engineering escalation brief: issue, affected scope, jurisdiction, discipline, document gaps, proposed reviewer and unanswered authority questions. Label drafts and unresolved issues. This is evidence review, not legal certification or operational approval.

## Tests

[Scenario specifications](references/scenarios.json) cover positive, negative, routing, freshness and human-authority cases. Their presence is not proof of model behavior; executed evidence belongs in the repository evaluation reports.
