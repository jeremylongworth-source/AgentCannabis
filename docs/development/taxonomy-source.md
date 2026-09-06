# Canadian Cannabis Skill Repository
# Master Taxonomy v1.0

**Status:** Frozen for roadmap development  
**Scope:** Canadian federally licensed commercial cannabis production  
**Atomic skills:** 233  
**Families:** 18

## Audit verdict

```text
CANADIAN_CANNABIS_MASTER_TAXONOMY_V1_READY
```

The v0.1 taxonomy contained 216 candidates.

Audit result:

```text
216 original candidates
+18 missing professional / regulatory capabilities
- 1 overly broad duplicate audit skill
---------------------------------------
233 v1 skills
```

Mass authoring is not yet authorized.

The next authorized artifact is the Codex development roadmap.

---

# Mandatory skill metadata

Every skill must declare:

```yaml
family:
tier:
production_stage:
jurisdiction:
licence_dependency:
responsible_role:
regulatory_sensitivity:
hazard_class:
human_approval_required:
source_freshness:
```

## Tier

```text
CORE
ADVANCED
SPECIALIST
```

## Regulatory sensitivity

```text
ROUTINE
REGULATED
HIGHLY_REGULATED
```

## Hazard class

```text
ROUTINE_PROCESS
CONTROLLED_PROCESS
HAZARDOUS_PROCESS
ENGINEERING_BOUNDARY
```

## Jurisdiction

```text
CANADA_FEDERAL
PROVINCIAL_REQUIRED
CONTEXTUAL
```

---

# FAMILY 01
# Regulatory, Licensing & Authorized Activities

**Count: 12**

```text
classify-cannabis-business-activity
identify-required-cannabis-licence
identify-applicable-licence-class
determine-authorized-cannabis-activity
review-licence-condition
identify-authorized-site-area
identify-cannabis-product-authority
identify-research-development-authority
identify-analytical-testing-authority
identify-licence-change-requirement
identify-regulatory-notification-requirement
verify-cannabis-regulatory-source-freshness
```

Default:

```text
Tier: CORE
Jurisdiction: CANADA_FEDERAL
Sensitivity: HIGHLY_REGULATED
Freshness: HIGH
```

---

# FAMILY 02
# Site Roles, Security & Facility Governance

**Count: 10**

```text
identify-required-site-roles
map-site-role-responsibilities
identify-responsible-person-obligation
identify-master-grower-responsibility
identify-qap-responsibility
identify-head-of-security-responsibility
review-site-access-governance
review-cannabis-storage-security
review-physical-security-requirement
assess-site-change-governance
```

---

# FAMILY 03
# Genetics, Starting Material & Propagation

**Count: 12**

```text
review-starting-material-provenance
classify-cannabis-starting-material
review-cultivar-identification
maintain-genetic-lineage-record
plan-propagation-workflow
review-propagation-readiness
assess-clone-establishment
assess-seedling-establishment
review-mother-stock-condition
identify-propagation-deviation
analyze-propagation-loss
prepare-propagation-batch-record
```

---

# FAMILY 04
# Cultivation Systems & Crop Planning

**Count: 12**

```text
classify-cultivation-system
build-crop-production-plan
build-crop-cycle-schedule
review-growing-area-capacity
plan-crop-space-allocation
review-crop-density-strategy
analyze-crop-uniformity
forecast-crop-output
review-cultivation-workflow
identify-cultivation-bottleneck
analyze-yield-deviation
compare-cultivation-scenarios
```

---

# FAMILY 05
# Environmental & Controlled-Growing Systems

**Count: 13**

```text
build-environment-monitoring-plan
review-growing-environment
analyze-temperature-deviation
analyze-humidity-deviation
analyze-airflow-deviation
review-lighting-strategy
review-photoperiod-control
review-environmental-uniformity
review-co2-management-context
analyze-environmental-trend
identify-environment-control-failure
investigate-climate-related-crop-stress
review-environment-sensor-coverage
```

---

# FAMILY 06
# Root Zone, Irrigation & Crop Inputs

**Count: 12**

```text
classify-growing-medium
review-root-zone-condition
build-irrigation-monitoring-plan
review-irrigation-performance
analyze-irrigation-deviation
review-drainage-performance
review-fertigation-strategy
review-crop-input-record
identify-crop-input-deviation
assess-water-quality-record
analyze-root-zone-trend
investigate-root-zone-stress
```

---

# FAMILY 07
# Plant Health, Pest & Disease Management

**Count: 13**

```text
build-plant-health-monitoring-plan
identify-plant-health-deviation
classify-pest-observation
classify-disease-symptom
assess-nonchemical-control-options
verify-pest-control-product-authority
review-pest-control-label-applicability
review-ipm-strategy
review-treatment-record
assess-treatment-effectiveness
analyze-pest-trend
investigate-crop-health-event
build-plant-health-corrective-action
```

Pest-control authorization must be checked against current Canadian sources rather than static repository lists.

---

# FAMILY 08
# Crop Management, Monitoring & Harvest

**Count: 12**

```text
build-crop-monitoring-plan
review-crop-observation-record
assess-crop-development-stage
review-canopy-management-plan
review-plant-support-strategy
identify-crop-development-deviation
assess-harvest-readiness
build-harvest-plan
plan-harvest-lot-segregation
review-harvest-record
analyze-harvest-loss
investigate-harvest-deviation
```

---

# FAMILY 09
# Post-Harvest Intake, Handling & Trimming

**Count: 10**

```text
plan-post-harvest-material-flow
verify-harvest-lot-identity
review-post-harvest-intake
plan-post-harvest-segregation
review-trimming-process
review-material-handling-control
assess-post-harvest-contamination-risk
review-post-harvest-hold-status
analyze-post-harvest-loss
investigate-post-harvest-handling-deviation
```

---

# FAMILY 10
# Drying, Curing, Storage & Stability

**Count: 13**

```text
build-drying-monitoring-plan
review-drying-environment
analyze-drying-trend
identify-drying-deviation
review-drying-endpoint-evidence
interpret-water-activity-result
review-moisture-result
assess-post-harvest-microbial-risk
plan-cure-monitoring
analyze-curing-condition
analyze-moisture-rebound
review-storage-condition
investigate-post-harvest-quality-loss
```

These remain measurement- and evidence-driven rather than fixed curing recipes.

---

# FAMILY 11
# Processing & Refinement Governance

**Count: 12**

```text
classify-cannabis-processing-method
verify-processing-licence-authority
map-cannabis-processing-flow
review-processing-material-intake
review-mechanical-separation-process
review-processing-batch-record
review-product-transformation-record
identify-processing-deviation
review-processing-yield-reconciliation
assess-processing-change
review-process-validation-evidence
prepare-processing-deviation-summary
```

Detailed extraction operation remains outside the general-purpose core.

---

# FAMILY 12
# Hazardous Processing & Preventive Controls

**Count: 12**

```text
classify-processing-hazard
classify-hazardous-extraction-operation
build-process-hazard-analysis
identify-biological-processing-hazard
identify-chemical-processing-hazard
identify-physical-processing-hazard
review-process-control-measure
identify-critical-control-point
review-critical-limit-evidence
review-corrective-action-procedure
verify-preventive-control-plan
identify-engineering-escalation
```

Defaults:

```text
Tier: ADVANCED
Sensitivity: HIGHLY_REGULATED
Hazard: HAZARDOUS_PROCESS / ENGINEERING_BOUNDARY
Human approval: REQUIRED
```

The repository does not replace professional engineering, fire-code review, pressure-system design, hazardous-location electrical design, or other qualified technical approval.

---

# FAMILY 13
# GPP, Sanitation & Quality Systems

**Count: 23**

Original:

```text
draft-cannabis-sop
review-cannabis-sop
assess-sop-change
document-sop-deviation
assess-gpp-impact-of-deviation
verify-sop-training-readiness
audit-sop-execution-record
review-sanitation-program
review-equipment-cleaning-program
review-personnel-hygiene-control
review-building-gpp-condition
review-air-filtration-ventilation-control
review-cross-contamination-control
review-storage-gpp-compliance
build-gpp-corrective-action
```

Added during audit:

```text
review-equipment-maintenance-program
review-calibration-program
review-document-control-system
assess-controlled-change
verify-personnel-training-record
review-facility-maintenance-program
review-supplier-qualification
review-ingredient-material-qualification
```

These additions close a major commercial quality-system gap.

---

# FAMILY 14
# Laboratory Testing & Quality Assurance

**Count: 16**

```text
build-cannabis-sampling-plan
review-sample-integrity
review-certificate-of-analysis
interpret-cannabinoid-test-result
review-pesticide-test-result
review-microbial-test-result
review-chemical-contaminant-result
review-heavy-metal-result
review-residual-solvent-result
assess-stability-data
identify-out-of-specification-result
investigate-out-of-specification-result
prepare-quality-release-package
assess-lot-release-readiness
build-product-stability-program
analyze-quality-trend
```

Added:

```text
build-product-stability-program
analyze-quality-trend
```

Lot-release authority remains with the appropriate regulated human role.

---

# FAMILY 15
# Product Classification, Formulation & Packaging

**Count: 14**

```text
classify-cannabis-product
identify-product-class-requirements
review-product-composition
review-formulation-record
review-ingredient-compliance
review-cannabinoid-uniformity
identify-product-thc-limit
identify-product-notification-requirement
review-packaging-readiness
review-labelling-readiness
verify-lot-number-traceability
review-storage-labelling-requirement
review-product-specification
prepare-new-cannabis-product-notice
```

Added:

```text
review-product-specification
prepare-new-cannabis-product-notice
```

The notification skill prepares compliance material. Submission remains the licence holder’s responsibility.

---

# FAMILY 16
# Inventory, Lot Lineage, CTLS & Excise

**Count: 16**

```text
reconcile-cannabis-inventory
map-cannabis-lot-lineage
map-cannabis-inventory-transformation
reconcile-packaged-inventory
reconcile-unpackaged-inventory
identify-inventory-discrepancy
investigate-unaccounted-cannabis
review-ctls-report-readiness
identify-ctls-reporting-discrepancy
validate-monthly-inventory-balance
identify-excise-licence-requirement
identify-cannabis-stamping-requirement
plan-cannabis-destruction
review-cannabis-destruction-record
classify-cannabis-loss-theft-event
prepare-loss-theft-reporting-package
```

Added:

```text
plan-cannabis-destruction
review-cannabis-destruction-record
classify-cannabis-loss-theft-event
prepare-loss-theft-reporting-package
```

CTLS currently accounts for packaged/unpackaged inventory reductions including destroyed and lost/stolen quantities. citeturn845166search1

---

# FAMILY 17
# Complaints, Recalls & Post-Market Surveillance

**Count: 11**

```text
triage-cannabis-quality-complaint
investigate-cannabis-quality-complaint
assess-product-hold-requirement
assess-recall-trigger
build-cannabis-recall-scope
review-mock-recall-performance
reconcile-recall-inventory
assess-adverse-reaction-reportability
build-post-market-corrective-action
prepare-serious-adverse-reaction-report
prepare-annual-adverse-reaction-summary
```

Added:

```text
prepare-serious-adverse-reaction-report
prepare-annual-adverse-reaction-summary
```

Human/regulatory approval remains required before submission.

---

# FAMILY 18
# Safety, Compliance Audit & Continuous Improvement

**Count: 10**

```text
identify-cannabis-workplace-hazard
build-cannabis-safety-risk-register
review-worker-training-requirement
review-whmis-readiness
review-lockout-control
review-facility-safety-deviation
audit-cannabis-compliance-record
perform-production-root-cause-analysis
build-corrective-preventive-action-plan
measure-production-improvement
```

Removed:

```text
audit-production-batch-record
```

Reason:

It duplicated more specific batch-record review functions already present in cultivation, propagation, processing and quality families.

---

# Final count

```text
01 Regulatory, Licensing & Authorized Activities       12
02 Site Roles, Security & Facility Governance          10
03 Genetics, Starting Material & Propagation           12
04 Cultivation Systems & Crop Planning                 12
05 Environmental & Controlled-Growing Systems          13
06 Root Zone, Irrigation & Crop Inputs                 12
07 Plant Health, Pest & Disease Management             13
08 Crop Management, Monitoring & Harvest               12
09 Post-Harvest Intake, Handling & Trimming            10
10 Drying, Curing, Storage & Stability                 13
11 Processing & Refinement Governance                  12
12 Hazardous Processing & Preventive Controls          12
13 GPP, Sanitation & Quality Systems                   23
14 Laboratory Testing & Quality Assurance              16
15 Product Classification, Formulation & Packaging     14
16 Inventory, Lot Lineage, CTLS & Excise               16
17 Complaints, Recalls & Post-Market Surveillance      11
18 Safety, Compliance Audit & Continuous Improvement   10
                                                        ---
TOTAL                                                  233
```

---

# Audit conclusions

## Atomicity

```text
READY
```

The remaining broad skills have bounded outputs and do not warrant further decomposition before implementation.

## Naming

```text
READY
```

Names are verb-led and suitable for AgentSkills-style routing.

## Cultivation scope

```text
READY
```

Cultivation skills focus on:

```text
planning
monitoring
diagnostics
records
quality
deviations
commercial production analysis
```

rather than fixed recreational grow recipes.

## Post-harvest scope

```text
READY
```

Drying and curing remain measurement-led and quality-oriented.

## Processing scope

```text
READY
```

General processing knowledge covers:

```text
classification
flow
batch records
deviations
validation
preventive controls
quality
hazard escalation
```

Hazardous-process operating procedures remain gated.

## Quality-system completeness

```text
READY
```

The v1 audit now explicitly covers:

```text
SOPs
training
document control
change control
maintenance
calibration
supplier qualification
ingredient/material qualification
sanitation
deviations
CAPA
testing
stability
release
quality trending
```

## Traceability completeness

```text
READY
```

The taxonomy now includes:

```text
lot lineage
transformations
packaged inventory
unpackaged inventory
CTLS
excise
destruction
loss/theft
```

## Post-market completeness

```text
READY
```

It now covers:

```text
complaints
holds
recalls
mock recalls
inventory reconciliation
adverse-reaction assessment
serious adverse-reaction reports
annual summaries
corrective action
```

---

# Sensitive-process routing

```text
REQUEST
   ↓
classify-cannabis-business-activity
   ↓
identify-required-cannabis-licence
   ↓
determine-authorized-cannabis-activity
   ↓
identify-responsible-role
   ↓
classify-processing-hazard
   ↓
┌──────────────────┬────────────────────┬─────────────────────┐
│ ROUTINE_PROCESS  │ CONTROLLED_PROCESS │ HAZARDOUS /         │
│                  │                    │ ENGINEERING         │
└────────┬─────────┴─────────┬──────────┴─────────┬───────────┘
         │                   │                    │
 normal skill        regulated skill       human / engineering
 routing             + source checks       authority required
```

---

# Human-authority boundaries

Human approval should be mandatory for skills involving:

```text
QAP lot release
regulatory submission
recall decisions
serious adverse-reaction reporting
hazardous processing
engineering controls
licence interpretation
provincial fire/building compliance
```

---

# Professional skillsets

## Cultivation

```text
cultivation-technician
cultivation-manager-support
master-grower-support
plant-health-specialist
controlled-environment-cultivation-specialist
```

## Post-harvest

```text
post-harvest-technician
drying-curing-specialist
post-harvest-manager
```

## Processing

```text
cannabis-processing-technician
processing-manager-support
preventive-controls-specialist
```

## Quality & compliance

```text
quality-control-specialist
qap-support
cannabis-quality-systems-specialist
cannabis-compliance-specialist
ctls-inventory-specialist
```

## Management

```text
cannabis-production-manager
cannabis-operations-manager
```

---

# Jurisdiction architecture

```text
specializations/
    canada/
        federal/
        ontario/
        british-columbia/
        alberta/
        quebec/
        ...
```

Federal production authority is foundational.

Provincial overlays may govern:

```text
occupational safety
fire code
building requirements
hazardous extraction
environmental controls
worker requirements
distribution interfaces
```

---

# Post-v1 specialist candidates

Do not place these automatically into the core roadmap:

```text
industrial-hemp
advanced-laboratory-methods
advanced-process-validation
advanced-extraction-engineering
environmental-compliance
specialized-fire-code-analysis
provincial-distribution
cannabis-research-licensing
```

---

# Final v1 verdict

```text
Taxonomy coverage: READY
Atomicity: READY
Naming: READY
Licence routing: READY
Role routing: READY
Cultivation architecture: READY
Post-harvest architecture: READY
Processing architecture: READY
Hazard classification: READY
GPP / quality systems: READY
Testing / QAP support: READY
CTLS / inventory: READY
Post-market controls: READY
Provincial overlay model: READY

Mass skill authoring: NOT YET AUTHORIZED
Codex roadmap creation: AUTHORIZED
```

Completion token:

```text
CANADIAN_CANNABIS_MASTER_TAXONOMY_V1_READY
```