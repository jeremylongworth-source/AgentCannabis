---
name: build-crop-monitoring-plan
description: "Prepare an auditable observation-record plan from existing approved site procedures. Use for build crop monitoring plan; review assistance only."
license: MIT
metadata:
  family: "08"
  tier: "CORE"
  production_stage: "crop-and-harvest-records"
  jurisdiction: "CANADA_FEDERAL"
  licence_dependency: "Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns"
  responsible_role: "Master Grower responsibility / authorized records reviewer"
  regulatory_sensitivity: "REGULATED"
  hazard_class: "ROUTINE_PROCESS"
  human_approval_required: "false-for-review-only; required-before-implementation"
  source_freshness: "HIGH: reverify at decision time; repository review interval 30 days; access date is not legal currency"
  package_kind: "atomic"
---

# Build crop monitoring plan

## Triggers

Prepare an auditable observation-record plan from existing approved site procedures.

## Non-triggers

No cultivation instructions, growing setpoints, irrigation/light/nutrient interventions, harvest timing or potency/yield optimization. The deliverable is observation governance.

## Inputs

Existing monitoring SOP/version, lot and area register, approved observation schedule, observer roles, instrument register, example records and escalation responsibilities.

## Assumptions and dependencies

Use [the review contract](references/review-contract.md). Do not assume absent licence, source, measurement or approval evidence. This package is self-contained; no other installed skill is required.

## Licence requirements and responsible role

Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns. Review owner: Master Grower responsibility / authorized records reviewer.

## Procedure

1. Define the record scope by site area, lot, observation category and reporting period; retain the schedule and criteria from the supplied approved SOP without inventing growing targets.
2. Map each required observation to a record field, observer, timestamp/timezone, unit where applicable, instrument identity and evidence location.
3. Identify missing observations, gaps in lot coverage, inconsistent units, calibration provenance and ambiguous handoffs; distinguish absent data from a normal result.
4. Create an exception route to the named reviewer using the site's existing escalation criteria. Leave absent criteria unresolved for that reviewer rather than proposing production adjustments.

## Evidence and source requirements

Retain record IDs, versions, dates, units/basis and provenance. Consult relevant entries in [the source snapshot](references/sources.json), then reverify the specific current primary authority and applicability. Missing or stale evidence remains an explicit gap.

## Hazard behavior and human approval

No cultivation instructions, growing setpoints, irrigation/light/nutrient interventions, harvest timing or potency/yield optimization. The deliverable is observation governance. Authorized humans retain release, filing, recall and engineering decisions.

## Outputs and limitations

Draft monitoring-record matrix with field, lot/area coverage, source SOP, responsible observer, supplied schedule, evidence link, missing-data treatment and review owner. Label drafts and unresolved issues. This is evidence review, not legal certification or operational approval.

## Tests

[Scenario specifications](references/scenarios.json) cover positive, negative, routing, freshness and human-authority cases. Their presence is not proof of model behavior; executed evidence belongs in the repository evaluation reports.
