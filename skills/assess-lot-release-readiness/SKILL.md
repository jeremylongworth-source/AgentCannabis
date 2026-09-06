---
name: assess-lot-release-readiness
description: "Assess whether a lot has a complete quality evidence package for an authorized human release decision. Use for assess lot release readiness; review assistance only."
license: MIT
metadata:
  family: "14"
  tier: "CORE"
  production_stage: "testing-and-quality"
  jurisdiction: "CANADA_FEDERAL"
  licence_dependency: "Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns"
  responsible_role: "QAP responsibility / authorized quality reviewer"
  regulatory_sensitivity: "HIGHLY_REGULATED"
  hazard_class: "CONTROLLED_PROCESS"
  human_approval_required: "true"
  source_freshness: "HIGH: reverify at decision time; repository review interval 30 days; access date is not legal currency"
  package_kind: "atomic"
---

# Assess lot release readiness

## Triggers

Assess whether a lot has a complete quality evidence package for an authorized human release decision.

## Non-triggers

No release authorization, fabricated approval, hold removal, test-result concealment or assumption that one COA proves overall compliance.

## Inputs

Lot identity/lineage, product class/specification/version, representative-sampling evidence, complete applicable testing/COAs, deviations/CAPA, batch records, packaging/labelling evidence, hold status and authorized quality responsibility.

## Assumptions and dependencies

Use [the review contract](references/review-contract.md). Do not assume absent licence, source, measurement or approval evidence. This package is self-contained; no other installed skill is required.

## Licence requirements and responsible role

Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns. Review owner: QAP responsibility / authorized quality reviewer.

## Procedure

1. Reconcile lot identity across batch, sampling, COA, inventory and packaging records. A matching product name alone is insufficient to establish that a COA covers the affected lot.
2. Map each applicable specification and required test to method, result, units/basis, sample identity and acceptance evidence. Preserve uncertainty when sampling representativeness or method applicability is missing.
3. Review open deviations, unresolved out-of-specification findings, retest rationale, traceability and existing holds. Do not use a passing retest or one passing microbial result to erase contradictory evidence.
4. List complete, missing and conflicting evidence for the authorized human working under applicable QAP responsibility. Keep the review conclusion distinct from batch approval or a hold removal.

## Evidence and source requirements

Retain record IDs, versions, dates, units/basis and provenance. Consult relevant entries in [the source snapshot](references/sources.json), then reverify the specific current primary authority and applicability. Missing or stale evidence remains an explicit gap.

## Hazard behavior and human approval

No release authorization, fabricated approval, hold removal, test-result concealment or assumption that one COA proves overall compliance. Authorized humans retain release, filing, recall and engineering decisions.

## Outputs and limitations

Release-readiness gap matrix, unresolved-risk summary and indexed draft quality package; explicit authorized-human decision pending. Label drafts and unresolved issues. This is evidence review, not legal certification or operational approval.

## Tests

[Scenario specifications](references/scenarios.json) cover positive, negative, routing, freshness and human-authority cases. Their presence is not proof of model behavior; executed evidence belongs in the repository evaluation reports.
