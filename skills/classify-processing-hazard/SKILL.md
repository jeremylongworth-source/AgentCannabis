---
name: classify-processing-hazard
description: "Classify a processing review request and determine whether qualified technical escalation is required. Use for classify processing hazard; review assistance only."
license: MIT
metadata:
  family: "12"
  tier: "ADVANCED"
  production_stage: "hazard-review"
  jurisdiction: "CANADA_FEDERAL"
  licence_dependency: "Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns"
  responsible_role: "QAP responsibility / authorized quality reviewer"
  regulatory_sensitivity: "HIGHLY_REGULATED"
  hazard_class: "HAZARDOUS_PROCESS"
  human_approval_required: "true"
  source_freshness: "HIGH: reverify at decision time; repository review interval 30 days; access date is not legal currency"
  package_kind: "atomic"
---

# Classify processing hazard

## Triggers

Classify a processing review request and determine whether qualified technical escalation is required.

## Non-triggers

No solvent extraction procedures, process settings, pressure-system tuning, protective-system design, interlock bypass or equipment restart advice.

## Inputs

Non-operational activity summary, material safety identifiers, equipment identity, site/province, existing hazard assessments, engineering-document references and named safety/quality owners.

## Assumptions and dependencies

Use [the review contract](references/review-contract.md). Do not assume absent licence, source, measurement or approval evidence. This package is self-contained; no other installed skill is required.

## Licence requirements and responsible role

Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns. Review owner: QAP responsibility / authorized quality reviewer.

## Procedure

1. Separate record-review questions from requested equipment operation, configuration or bypasses; operational boundary requests receive a safe redirection before further routing.
2. Identify reported biological, chemical and physical contamination concerns separately from flammable materials, stored pressure, fire/explosion, critical ventilation and hazardous electrical concerns.
3. Assign the most consequential supported route among ROUTINE_PROCESS, CONTROLLED_PROCESS, HAZARDOUS_PROCESS and ENGINEERING_BOUNDARY; incomplete hazard information remains unresolved, never implicitly routine.
4. Prepare a bounded handoff naming missing evidence, affected scope, responsible professionals and the actual province/authority questions. Do not certify that controls are adequate or equipment may restart.

## Evidence and source requirements

Retain record IDs, versions, dates, units/basis and provenance. Consult relevant entries in [the source snapshot](references/sources.json), then reverify the specific current primary authority and applicability. Missing or stale evidence remains an explicit gap.

## Hazard behavior and human approval

No solvent extraction procedures, process settings, pressure-system tuning, protective-system design, interlock bypass or equipment restart advice. Authorized humans retain release, filing, recall and engineering decisions.

## Outputs and limitations

Hazard-routing record with reported hazard, evidence, uncertainty, class, rationale and qualified-review handoff. Label drafts and unresolved issues. This is evidence review, not legal certification or operational approval.

## Tests

[Scenario specifications](references/scenarios.json) cover positive, negative, routing, freshness and human-authority cases. Their presence is not proof of model behavior; executed evidence belongs in the repository evaluation reports.
