---
name: determine-authorized-cannabis-activity
description: "Compare a described activity with documented licence authority and current primary requirements. Use for determine authorized cannabis activity; review assistance only."
license: MIT
metadata:
  family: "01"
  tier: "CORE"
  production_stage: "federal-governance"
  jurisdiction: "CANADA_FEDERAL"
  licence_dependency: "Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns"
  responsible_role: "Responsible Person / authorized regulatory reviewer"
  regulatory_sensitivity: "HIGHLY_REGULATED"
  hazard_class: "ROUTINE_PROCESS"
  human_approval_required: "true"
  source_freshness: "HIGH: reverify at decision time; repository review interval 30 days; access date is not legal currency"
  package_kind: "atomic"
---

# Determine authorized cannabis activity

## Triggers

Compare a described activity with documented licence authority and current primary requirements.

## Non-triggers

Do not confer licensing, treat a claimed class as proof, or make a binding legal determination. Do not turn a finding of documented authority into operational production instructions.

## Inputs

Activity/material/product description, jurisdiction, licence class/subclass and validity, licence conditions/amendments, site/area, current statutory provisions and responsible-role evidence.

## Assumptions and dependencies

Use [the review contract](references/review-contract.md). Do not assume absent licence, source, measurement or approval evidence. This package is self-contained; no other installed skill is required.

## Licence requirements and responsible role

Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns. Review owner: Responsible Person / authorized regulatory reviewer.

## Procedure

1. Decompose the request into distinct activities and identify the material/product and purpose of each; do not let a mixed workflow inherit permission from one licensed step.
2. Compare each activity with the current class/subclass provision and the actual licence, conditions, amendments and authorized site/area; cite the precise evidence for every match or conflict.
3. Distinguish ancillary cultivation authority from general processing authority, and separately check sale, testing and research contexts instead of treating them as implied permissions.
4. Identify the responsible human reviewer and unresolved exceptions. A missing licence permits general research and a gap list, but not an affirmative site-specific authorization conclusion.

## Evidence and source requirements

Retain record IDs, versions, dates, units/basis and provenance. Consult relevant entries in [the source snapshot](references/sources.json), then reverify the specific current primary authority and applicability. Missing or stale evidence remains an explicit gap.

## Hazard behavior and human approval

Do not confer licensing, treat a claimed class as proof, or make a binding legal determination. Do not turn a finding of documented authority into operational production instructions. Authorized humans retain release, filing, recall and engineering decisions.

## Outputs and limitations

Activity-authority matrix with activity, cited requirement, licence evidence, condition/area restriction, uncertainty, proposed human reviewer and bounded conclusion. Label drafts and unresolved issues. This is evidence review, not legal certification or operational approval.

## Tests

[Scenario specifications](references/scenarios.json) cover positive, negative, routing, freshness and human-authority cases. Their presence is not proof of model behavior; executed evidence belongs in the repository evaluation reports.
