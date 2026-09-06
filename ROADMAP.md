# Canadian Cannabis Skill Repository Development Roadmap

**Project name:** TBD  
**Working identifier:** Canadian Cannabis Skill Repository  
**Wave prefix:** `CC`  
**Repository path:** TBD  
**Roadmap version:** 0.1  
**Taxonomy authority:** Canadian Cannabis Skill Repository Master Taxonomy v1.0  
**Atomic skills:** 233  
**Primary jurisdiction:** Canada  
**Current execution target:** `CC-00`

---

# 1. Mission

Build an open-source AI skill repository for professional Canadian commercial cannabis operations covering:

```text
Cultivation
Post-harvest
Drying and curing
Processing and refinement governance
Good Production Practices
Quality assurance
Analytical testing
Inventory and traceability
CTLS reporting
Excise interfaces
Product classification
Packaging and labelling
Complaints and recalls
Operational safety
Continuous improvement
```

The repository is intended for lawful professional decision support in regulated Canadian cannabis operations.

It does not itself confer:

```text
Health Canada licensing
QAP authority
Master Grower status
regulatory approval
laboratory accreditation
professional engineering approval
fire-code approval
occupational certification
```

---

# 2. Core Architecture Principle

```text
LICENCE BEFORE ACTIVITY
        ↓
ROLE BEFORE DECISION
        ↓
GPP BEFORE PRODUCTION
        ↓
EVIDENCE BEFORE RELEASE
        ↓
ENGINEERING BEFORE HAZARDOUS PROCESS
```

Health Canada currently distinguishes cultivation and processing authorities. Cultivation licences permit growing and limited indoor post-harvest activities such as drying, trimming and milling, while processing licences cover harvested cannabis processing and broader product manufacture. citeturn508526search6turn508526search2

---

# 3. Production Architecture

```text
                      CANADA FEDERAL CORE
                             │
                 LICENSING / AUTHORITY
                             │
                SITE ROLES / GOVERNANCE
                             │
                       GPP / QUALITY
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
  CULTIVATION          POST-HARVEST        PROCESSING &
                       DRYING/CURING        REFINEMENT
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                   TESTING / QAP SUPPORT
                             │
                 PRODUCT / PACKAGING
                             │
                 INVENTORY / CTLS / CRA
                             │
                  POST-MARKET CONTROL
                             │
                    PROVINCIAL LAYERS
```

---

# 4. Skill Classification Model

Every skill must contain:

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

## Hazard classification

```text
ROUTINE_PROCESS
CONTROLLED_PROCESS
HAZARDOUS_PROCESS
ENGINEERING_BOUNDARY
```

---

# 5. Hazardous-Process Router

Processing-related tasks must not jump directly to operational guidance.

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
┌──────────────────┬────────────────────┬────────────────────┐
│ ROUTINE_PROCESS  │ CONTROLLED_PROCESS │ HAZARDOUS /        │
│                  │                    │ ENGINEERING        │
└────────┬─────────┴─────────┬──────────┴─────────┬──────────┘
         │                   │                    │
 normal skill        regulated controls      qualified human /
 routing             + source checks         engineered system
```

---

# 6. Repository Boundaries

Agent skills may support:

```text
production planning
crop monitoring
plant-health diagnostics
environmental analysis
post-harvest quality
drying/curing analysis
process classification
process-flow review
GPP
SOPs
preventive controls
testing interpretation
quality investigations
inventory reconciliation
traceability
CTLS preparation
regulatory research
CAPA
continuous improvement
```

The general repository should not provide procedural instruction primarily intended for:

```text
unlicensed cannabis production
psychoactive-potency optimization
hazardous solvent extraction operation
pressure-system configuration
flammable-gas extraction operation
safety-interlock bypass
explosion-protection engineering
hazardous-location electrical design
fire-protection engineering
```

Hazardous commercial processes remain professional and engineering boundaries.

---

# 7. Wave Gate Model

Each development wave ends:

```text
READY
PARTIALLY_READY
BLOCKED
```

Every wave must produce:

```text
final handoff
completion token
validation evidence
known limitations
unresolved issues
recommended next wave
```

Do not silently carry unresolved work forward.

---

# CC-00
# Repository Discovery & Baseline

## Objective

Establish repository truth before implementation.

## Codex tasks

1. Locate or initialize the project repository as appropriate.
2. Inspect:
   - Git state;
   - branch;
   - remote;
   - existing files;
   - documentation;
   - tooling;
   - tests;
   - skill structures.
3. Review AgentSkills, ChefSkills, AgentLogistics and AgentInvestigate only as structural references where available.
4. Record reusable patterns.
5. Identify cannabis-specific architecture that must differ.

## Required artifact

```text
docs/development/CC-00-baseline-audit.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_00_BASELINE_READY
```

---

# CC-01
# Domain & Scope Contract

## Objective

Freeze what the repository is and is not.

Define:

```text
commercial cannabis
cultivation
post-harvest
drying
curing
processing
refinement
quality assurance
testing
traceability
provincial overlays
industrial hemp boundary
```

Explicitly distinguish professional decision support from consumer growing guidance.

## Required artifacts

```text
docs/architecture/domain-contract.md
docs/architecture/scope-boundaries.md
docs/architecture/prohibited-capabilities.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_01_DOMAIN_CONTRACT_READY
```

---

# CC-02
# Master Taxonomy Integration

## Objective

Convert the approved 233-skill taxonomy into repository authority.

## Required artifacts

```text
docs/architecture/master-taxonomy-v1.md
docs/architecture/taxonomy-index.yaml
```

Each skill must receive complete metadata.

## Gate

One canonical taxonomy exists.

## Completion token

```text
CANADIAN_CANNABIS_CC_02_MASTER_TAXONOMY_READY
```

---

# CC-03
# Licence, Role & Activity Routing

## Objective

Implement the repository's main regulatory gate.

## Build routing for

```text
licence class
authorized activities
licence conditions
authorized site areas
production stage
regulated site role
required human approval
```

Health Canada currently states that licence type defines authorized activities and individual licence conditions can further restrict those activities. citeturn508526search2

## Required artifacts

```text
docs/architecture/licence-routing.md
docs/architecture/site-role-routing.md
docs/architecture/activity-authority-contract.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_03_LICENCE_ROUTING_READY
```

---

# CC-04
# Hazard & Engineering Boundary

## Objective

Define safe processing behavior before processing skills exist.

Formalize:

```text
ROUTINE_PROCESS
CONTROLLED_PROCESS
HAZARDOUS_PROCESS
ENGINEERING_BOUNDARY
```

Define escalation for:

- flammable materials;
- pressurized systems;
- hazardous chemicals;
- hazardous electrical environments;
- fire/explosion hazards;
- critical ventilation;
- building/fire-code implications.

## Required artifacts

```text
docs/architecture/process-hazard-model.md
docs/architecture/engineering-boundaries.md
docs/architecture/hazardous-process-routing.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_04_HAZARD_ROUTING_READY
```

---

# CC-05
# Skill Authoring Standard

## Objective

Define the package contract for all skills.

Required fields:

```text
name
description
triggers
non-triggers
inputs
assumptions
dependencies
licence requirements
responsible role
procedure
evidence
source requirements
hazard behavior
outputs
limitations
human approval
tests
```

## Required artifacts

```text
docs/standards/skill-authoring-standard.md
docs/standards/skill-naming-standard.md
docs/standards/output-contract-standard.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_05_SKILL_STANDARD_READY
```

---

# CC-06
# Regulatory Research & Source Standard

## Objective

Prevent stale cannabis-law content from spreading across skills.

## Source hierarchy

```text
1. Cannabis Act / Regulations
2. Health Canada
3. CRA
4. federal regulators
5. provincial statutes and regulators
6. recognized standards
7. peer-reviewed science
8. high-quality technical literature
9. secondary industry material
```

## Required metadata

```yaml
source_title:
organization:
jurisdiction:
authority_level:
source_url:
publication_date:
effective_date:
last_verified:
applicability:
supersession_risk:
used_by:
```

## Required artifacts

```text
docs/standards/research-and-evidence-standard.md
docs/standards/regulatory-source-standard.md
docs/standards/source-freshness-standard.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_06_SOURCE_STANDARD_READY
```

---

# CC-07
# GPP & Quality-System Standard

## Objective

Create shared quality rules before production authoring.

Define repository-wide handling of:

```text
SOPs
deviations
training
document control
change control
sanitation
equipment maintenance
calibration
supplier qualification
ingredient qualification
CAPA
quality review
```

GPP currently applies broadly across production, packaging, labelling, distribution, storage, sampling and testing and includes additional requirements for processing. citeturn508526search0turn508526search1

## Required artifact

```text
docs/standards/gpp-quality-system-standard.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_07_GPP_STANDARD_READY
```

---

# CC-08
# Testing & Evaluation Framework

## Objective

Prove correctness before mass authoring.

Create test classes for:

```text
correct skill routing
incorrect licence
missing licence
wrong jurisdiction
missing responsible role
stale regulatory source
missing evidence
unsafe process request
engineering-boundary request
incorrect calculation
unsupported assumption
quality-release overreach
output compliance
```

## Required artifacts

```text
docs/standards/testing-standard.md
docs/standards/evaluation-standard.md
tests/
scripts/
```

## Completion token

```text
CANADIAN_CANNABIS_CC_08_VALIDATION_FRAMEWORK_READY
```

---

# CC-09
# Shared Foundations

## Objective

Create reusable material only where real skills require it.

Potential assets:

```text
licence authority check
SOP template
deviation record
CAPA template
crop-monitoring record
batch record
post-harvest intake
drying-monitoring log
hazard analysis
sampling plan
COA review
lot-release package
inventory reconciliation
CTLS review
complaint record
recall assessment
```

## Rule

No empty reference library.

## Completion token

```text
CANADIAN_CANNABIS_CC_09_SHARED_FOUNDATIONS_READY
```

---

# CC-10
# Reference Skill Set

## Objective

Prove the architecture using representative skills before mass production.

Recommended reference skills:

### Routine

```text
build-crop-monitoring-plan
```

### Regulated

```text
determine-authorized-cannabis-activity
```

### Quality / human approval

```text
assess-lot-release-readiness
```

### Hazardous-process

```text
classify-processing-hazard
```

### Provincial dependency

```text
identify-engineering-escalation
```

Each must have:

```text
complete metadata
references
positive tests
negative tests
routing tests
source-freshness tests
human-authority tests
```

## Hard gate

Mass skill authoring is not authorized until `CC-10` closes READY.

## Completion token

```text
CANADIAN_CANNABIS_CC_10_REFERENCE_SKILLS_READY
```

---

# CC-11
# Federal Regulatory Core

## Objective

Build Family 01.

Implement all regulatory/licensing skills.

## Integration tests

Cover:

```text
cultivation licence
processing licence
nursery
micro vs standard
licence conditions
unauthorized activity
site-area restriction
testing authority
R&D authority
```

## Completion token

```text
CANADIAN_CANNABIS_CC_11_FEDERAL_REGULATORY_CORE_READY
```

---

# CC-12
# Site Roles, Security & Governance

## Objective

Build Family 02.

Include:

```text
Responsible Person
Master Grower
QAP
Head of Security
site access
storage security
facility changes
```

## Boundary

Agent support does not replace regulated site personnel.

## Completion token

```text
CANADIAN_CANNABIS_CC_12_SITE_GOVERNANCE_READY
```

---

# CC-13
# GPP, SOP & Quality Systems

## Objective

Build Family 13.

This should be one of the largest early waves.

Implement all skills covering:

```text
SOPs
training
sanitation
cleaning
cross-contamination
building conditions
ventilation
maintenance
calibration
document control
change control
supplier qualification
material qualification
CAPA
```

## Completion token

```text
CANADIAN_CANNABIS_CC_13_QUALITY_SYSTEMS_READY
```

---

# CC-14
# Genetics, Starting Material & Propagation

## Objective

Build Family 03.

Focus on:

```text
starting-material provenance
cultivar identity
genetic lineage
propagation planning
clone/seedling establishment
mother-stock monitoring
propagation records
deviations
```

## Completion token

```text
CANADIAN_CANNABIS_CC_14_PROPAGATION_READY
```

---

# CC-15
# Cultivation Systems & Crop Planning

## Objective

Build Family 04.

Build planning and diagnostic capabilities for:

```text
indoor
greenhouse
outdoor
crop cycles
capacity
space allocation
crop density
workflow
yield deviations
scenario analysis
```

Avoid universal potency-maximization recipes.

## Completion token

```text
CANADIAN_CANNABIS_CC_15_CULTIVATION_PLANNING_READY
```

---

# CC-16
# Environmental Growing Systems

## Objective

Build Family 05.

Cover:

```text
temperature
humidity
airflow
lighting
photoperiod
environmental uniformity
CO2 context
environmental trends
sensor coverage
control failures
crop stress
```

## Gate

Skills should reason from facility/crop data rather than assert one universal target profile.

## Completion token

```text
CANADIAN_CANNABIS_CC_16_ENVIRONMENT_READY
```

---

# CC-17
# Root Zone, Irrigation & Inputs

## Objective

Build Family 06.

Include:

```text
growing media
root-zone observations
irrigation
drainage
fertigation
crop inputs
water-quality records
trend analysis
deviation investigation
```

## Completion token

```text
CANADIAN_CANNABIS_CC_17_ROOT_ZONE_READY
```

---

# CC-18
# Plant Health, Pest & Disease Management

## Objective

Build Family 07.

## Mandatory routing

```text
plant-health observation
        ↓
nonchemical controls
        ↓
current authorized product verification
        ↓
label applicability
        ↓
documented treatment decision
```

Do not embed static approved-pesticide lists.

## Completion token

```text
CANADIAN_CANNABIS_CC_18_PLANT_HEALTH_READY
```

---

# CC-19
# Crop Management & Harvest

## Objective

Build Family 08.

Cover:

```text
monitoring
development stage
canopy-plan review
plant support
crop deviations
harvest readiness
harvest planning
lot segregation
harvest records
harvest loss
```

## Completion token

```text
CANADIAN_CANNABIS_CC_19_HARVEST_READY
```

---

# CC-20
# Post-Harvest Intake & Handling

## Objective

Build Family 09.

Required lifecycle:

```text
harvest lot
→ identity
→ intake
→ segregation
→ trimming
→ handling
→ contamination control
→ hold status
→ loss / deviation
```

## Completion token

```text
CANADIAN_CANNABIS_CC_20_POST_HARVEST_READY
```

---

# CC-21
# Drying, Curing, Storage & Stability

## Objective

Build Family 10.

Cover:

```text
drying monitoring
environment
trends
deviations
endpoint evidence
water activity
moisture
microbial risk
curing monitoring
moisture rebound
storage
quality loss
```

## Critical rule

Measured evidence and validated facility procedures outrank folklore or generalized grow advice.

## Completion token

```text
CANADIAN_CANNABIS_CC_21_DRYING_CURING_READY
```

---

# CC-22
# Processing & Refinement Governance

## Objective

Build Family 11.

Implement process-analysis capabilities for:

```text
method classification
licence authority
material intake
process flow
mechanical separation
batch records
product transformation
yield reconciliation
deviations
change review
validation evidence
```

## Boundary

Do not turn this wave into extraction-operation instructions.

## Completion token

```text
CANADIAN_CANNABIS_CC_22_PROCESSING_GOVERNANCE_READY
```

---

# CC-23
# Hazardous Processing & Preventive Controls

## Objective

Build Family 12.

## Implement

```text
hazard classification
hazard analysis
biological hazards
chemical hazards
physical hazards
control measures
critical-control-point identification
critical-limit evidence
corrective-action review
preventive-control-plan review
engineering escalation
```

Health Canada currently requires a written preventive control plan for specified extract and edible-cannabis activities. citeturn508526search0

## Hard boundary

No instructions for configuring or operating hazardous extraction equipment.

## Completion token

```text
CANADIAN_CANNABIS_CC_23_PREVENTIVE_CONTROLS_READY
```

---

# CC-24
# Laboratory Testing & Quality Assurance

## Objective

Build Family 14.

Cover:

```text
sampling
sample integrity
COA review
cannabinoids
pesticides
microbiology
chemical contaminants
heavy metals
residual solvents
stability
OOS
quality trending
release package
lot-release readiness
```

## Human gate

```text
AI review
    ↓
quality package
    ↓
QAP / authorized human decision
```

## Completion token

```text
CANADIAN_CANNABIS_CC_24_TESTING_QA_READY
```

---

# CC-25
# Product Classification, Formulation & Packaging

## Objective

Build Family 15.

Cover:

```text
product class
composition
formulation records
ingredients
uniformity
THC-limit identification
product notification
product specifications
packaging
labelling
lot traceability
storage labelling
```

## Completion token

```text
CANADIAN_CANNABIS_CC_25_PRODUCT_COMPLIANCE_READY
```

---

# CC-26
# Inventory, Lot Lineage, CTLS & Excise

## Objective

Build Family 16.

Cover:

```text
inventory reconciliation
lot lineage
transformations
packaged inventory
unpackaged inventory
inventory discrepancies
unaccounted cannabis
CTLS readiness
monthly balance validation
destruction
loss/theft
CRA excise
stamping
```

## Separation rule

Health Canada tracking and CRA excise are separate regulatory systems even when they use overlapping inventory information.

## Completion token

```text
CANADIAN_CANNABIS_CC_26_TRACEABILITY_READY
```

---

# CC-27
# Complaints, Recalls & Post-Market Control

## Objective

Build Family 17.

Cover:

```text
quality complaints
product holds
recall assessment
recall scope
mock recalls
recall inventory
adverse-reaction assessment
serious adverse-reaction package
annual summary
post-market corrective action
```

## Human gate

Recall and regulatory-reporting decisions remain with authorized humans.

## Completion token

```text
CANADIAN_CANNABIS_CC_27_POST_MARKET_READY
```

---

# CC-28
# Safety, Audit & Continuous Improvement

## Objective

Build Family 18.

Cover:

```text
workplace hazards
risk registers
worker-training requirements
WHMIS
lockout
facility safety deviations
compliance audits
root cause analysis
CAPA
improvement measurement
```

## Jurisdiction rule

Provincial safety rules must not be represented as universal federal cannabis rules.

## Completion token

```text
CANADIAN_CANNABIS_CC_28_SAFETY_IMPROVEMENT_READY
```

---

# CC-29
# Ontario Regulatory & Safety Overlay

## Objective

Build the first provincial specialization.

Path:

```text
specializations/canada/ontario/
```

Research current:

```text
occupational health and safety
fire code
building requirements
hazardous cannabis extraction
worker requirements
environmental considerations
```

No assumptions should be copied from other provinces.

## Completion token

```text
CANADIAN_CANNABIS_CC_29_ONTARIO_READY
```

---

# CC-30
# British Columbia Overlay

Path:

```text
specializations/canada/british-columbia/
```

Focus on:

```text
WorkSafeBC
worker hazards
facility safety
chemical hazards
processing hazards
provincial obligations
```

## Completion token

```text
CANADIAN_CANNABIS_CC_30_BRITISH_COLUMBIA_READY
```

---

# CC-31
# Alberta Overlay

Path:

```text
specializations/canada/alberta/
```

Build from Alberta-specific sources rather than cloning Ontario or B.C.

## Completion token

```text
CANADIAN_CANNABIS_CC_31_ALBERTA_READY
```

---

# CC-32
# Quebec Overlay

Path:

```text
specializations/canada/quebec/
```

Include bilingual-source handling where authoritative material is available in French.

## Completion token

```text
CANADIAN_CANNABIS_CC_32_QUEBEC_READY
```

---

# CC-33
# Provincial Expansion Framework

## Objective

Create the architecture for remaining Canadian jurisdictions.

## Required artifact

```text
docs/architecture/canadian-provincial-roadmap.md
```

Potential later modules:

```text
Manitoba
Saskatchewan
Nova Scotia
New Brunswick
Newfoundland and Labrador
Prince Edward Island
Yukon
Northwest Territories
Nunavut
```

## Completion token

```text
CANADIAN_CANNABIS_CC_33_PROVINCIAL_FRAMEWORK_READY
```

---

# CC-34
# Professional Skillset Composition

## Objective

Compose atomic skills into professional operating systems.

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

## Quality / compliance

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

Each skillset defines:

```text
purpose
included skills
routing triggers
dependencies
licence requirements
human-authority limits
hazard boundaries
expected outputs
excluded responsibilities
```

## Completion token

```text
CANADIAN_CANNABIS_CC_34_PROFESSIONAL_SKILLSETS_READY
```

---

# CC-35
# Multi-Skill Integration Evaluation

## Objective

Test end-to-end commercial workflows.

### Scenario A: Cultivation deviation

```text
crop monitoring
→ environment
→ irrigation
→ plant health
→ evidence
→ root cause
→ corrective action
```

### Scenario B: Post-harvest quality problem

```text
lot identity
→ drying records
→ moisture / water activity
→ storage
→ microbial evidence
→ hold
→ investigation
```

### Scenario C: Processing deviation

```text
licence authority
→ process flow
→ hazard classification
→ batch record
→ deviation
→ preventive controls
→ quality review
```

### Scenario D: Inventory discrepancy

```text
lot lineage
→ transformation
→ packaged inventory
→ CTLS records
→ destruction / loss
→ reconciliation
```

### Scenario E: Product release

```text
product class
→ specification
→ testing
→ COA
→ packaging
→ labelling
→ release-readiness
→ QAP decision
```

## Completion token

```text
CANADIAN_CANNABIS_CC_35_INTEGRATION_VALIDATED
```

---

# CC-36
# Adversarial Safety & Boundary Evaluation

## Objective

Verify that useful professional capabilities cannot easily be redirected into unsafe or out-of-scope instructions.

Test requests framed as:

```text
unlicensed production
maximum-potency optimization
home extraction
flammable-solvent extraction
pressure-system tuning
interlock bypass
unapproved pesticide use
falsified quality release
CTLS record manipulation
testing-result concealment
```

Expected response behavior:

```text
identify boundary
stop prohibited procedure
preserve safe professional assistance
redirect toward compliance / diagnostics / qualified human review
```

## Completion token

```text
CANADIAN_CANNABIS_CC_36_SAFETY_VALIDATED
```

---

# CC-37
# Specialized Expansion Framework

## Objective

Define post-core expansion without automatically authorizing it.

Candidates:

```text
industrial hemp
advanced laboratory methods
environmental compliance
research licensing
advanced process validation
specialized provincial distribution
```

High-risk specialist candidates:

```text
advanced extraction engineering
flammable-solvent systems
pressure systems
specialized fire-code engineering
```

These require separate architecture approval.

## Required artifact

```text
docs/architecture/specialization-roadmap.md
```

## Completion token

```text
CANADIAN_CANNABIS_CC_37_SPECIALIZATION_FRAMEWORK_READY
```

---

# CC-38
# Public Documentation & Repository Readiness

## Required public files

```text
README.md
ROADMAP.md
CONTRIBUTING.md
CHANGELOG.md
LICENSE
SECURITY.md
CODE_OF_CONDUCT.md
```

README should explain:

```text
what the repository is
who it serves
federal/provincial architecture
cultivation capabilities
post-harvest capabilities
processing boundaries
quality systems
skillsets
validation
limitations
contributing
```

## Completion token

```text
CANADIAN_CANNABIS_CC_38_PUBLIC_READINESS_READY
```

---

# CC-39
# v1 Release Candidate Audit

## Objective

Determine whether the project deserves v1 status.

Audit:

```text
taxonomy implementation
federal source integrity
source freshness
licence routing
role routing
GPP correctness
cultivation quality
post-harvest quality
processing boundaries
hazard routing
QAP boundaries
testing
CTLS reconciliation
provincial isolation
professional skillsets
safety behavior
documentation
repository hygiene
```

## Verdict

```text
V1_READY
V1_PARTIALLY_READY
V1_BLOCKED
```

## Completion token

```text
CANADIAN_CANNABIS_CC_39_V1_RC_AUDIT_COMPLETE
```

---

# 8. Standard Codex Execution Protocol

For every wave:

## Step 1: Read authority

Read:

```text
ROADMAP.md
latest final handoff
master taxonomy
domain contract
relevant standards
affected skills
```

## Step 2: Verify repository truth

Do not trust handoffs blindly.

Inspect current repository state.

## Step 3: Declare bounded scope

Record:

```text
IN SCOPE
OUT OF SCOPE
EXPECTED FILES
RESEARCH REQUIRED
VALIDATION REQUIRED
```

## Step 4: Research first

Current primary sources should precede implementation for:

```text
licensing
GPP
product rules
testing
CTLS
excise
pest controls
provincial safety
hazardous processing
```

## Step 5: Implement

Avoid unrelated refactoring.

## Step 6: Validate

Run applicable:

```text
structural validators
skill tests
routing tests
source checks
freshness checks
hazard tests
human-authority tests
integration tests
```

## Step 7: Review diff

Check for:

```text
scope creep
duplicated knowledge
stale sources
unsafe expansion
unsupported regulatory claims
missing tests
weakened human gates
```

## Step 8: Produce handoff

---

# 9. Standard Wave Handoff

Recommended path:

```text
docs/development/handoffs/
```

Naming:

```text
CC-XX-final-handoff.md
```

Required structure:

```text
# Wave

# Objective

# Verdict
READY | PARTIALLY_READY | BLOCKED

# Completion Token

# Scope Completed

# Files Added

# Files Modified

# Research Performed

# Sources

# Validation Performed

# Tests

# Regulatory / Quality Review

# Hazard / Safety Review

# Known Limitations

# Unresolved Issues

# Explicitly Not Completed

# Recommended Next Wave
```

---

# 10. Source Freshness Rules

High-change regulatory areas include:

```text
licence requirements
authorized activities
licence conditions
pest-control authorization
product composition
packaging
labelling
CTLS
excise
provincial safety
hazardous processing
```

They should carry:

```yaml
last_verified:
freshness_interval:
primary_authority:
supersession_risk:
```

Stale content becomes:

```text
REVERIFICATION_REQUIRED
```

not automatically false.

---

# 11. Test Fixture Strategy

Create fictional licensed producers rather than using real companies.

Recommended fixtures:

```text
tests/fixtures/
    micro-cultivation-site/
    standard-cultivation-site/
    micro-processing-site/
    standard-processing-site/
    post-harvest-quality-case/
    inventory-discrepancy-case/
    product-release-case/
    recall-case/
```

Fixtures may include:

```text
licence conditions
facility areas
crop records
environment records
batch records
COAs
inventory
CTLS data
SOPs
deviations
complaints
```

---

# 12. No-Silent-Assumption Rule

Example:

```text
Known:
The batch COA reports a compliant microbial result.

Unknown:
Whether the sampled material is representative of the entire affected lot.

Permitted:
Identify what evidence would establish sampling integrity.

Not permitted:
Automatically declare the lot releasable.
```

This reasoning discipline should apply repository-wide.

---

# 13. Immediate Development Sequence

Codex should initially execute only:

```text
CC-00 Repository Baseline
        ↓
CC-01 Domain Contract
        ↓
CC-02 Master Taxonomy
        ↓
CC-03 Licence / Role Routing
        ↓
CC-04 Hazard Boundary
        ↓
CC-05 Skill Standard
        ↓
CC-06 Source Standard
        ↓
CC-07 GPP Standard
        ↓
CC-08 Validation Framework
        ↓
CC-09 Shared Foundations
        ↓
CC-10 Reference Skills
```

Only after:

```text
CANADIAN_CANNABIS_CC_10_REFERENCE_SKILLS_READY
```

should Codex begin large-scale skill authoring.

---

# 14. Major Project Milestones

## Architecture proven

```text
CC-00 → CC-10
```

## Federal production foundation

```text
CC-11 → CC-13
```

## Cultivation system complete

```text
CC-14 → CC-19
```

## Post-harvest system complete

```text
CC-20 → CC-21
```

## Processing governance complete

```text
CC-22 → CC-23
```

## Quality / commercial lifecycle complete

```text
CC-24 → CC-28
```

## Initial provincial baseline

```text
CC-29 → CC-33
```

## Professional composition

```text
CC-34
```

## Integration + safety validation

```text
CC-35 → CC-36
```

## Public candidate

```text
CC-38
```

## v1 decision

```text
CC-39
```

---

# 15. First Codex Instruction

Use the following as the initial execution directive:

```text
Treat ROADMAP.md and the approved Canadian Cannabis Master Taxonomy v1.0
as planning authority, but treat the repository itself as execution truth.

Begin only with CC-00.

Do not implement future waves.

Inspect the repository and determine its actual current state.

Where accessible, compare structural patterns from AgentSkills, ChefSkills,
AgentLogistics, and AgentInvestigate, but do not automatically copy them.
This repository has distinct Canadian licensing, GPP, QAP, quality-system,
hazardous-process, provincial-jurisdiction, and regulatory-freshness
requirements.

Produce:

docs/development/CC-00-baseline-audit.md

Do not create the entire proposed directory structure simply because it
appears in the roadmap.

Close CC-00 with READY, PARTIALLY_READY, or BLOCKED.

Include the completion token only when justified:

CANADIAN_CANNABIS_CC_00_BASELINE_READY

Produce the required final handoff.

Recommend CC-01 only after CC-00 is genuinely closed.
```

---

# 16. Roadmap Status

```text
Roadmap version: 0.1
Taxonomy: FROZEN FOR DEVELOPMENT
Atomic skill count: 233

Current execution target:
CC-00

Architecture gate:
CC-10

Cultivation milestone:
CC-19

Post-harvest milestone:
CC-21

Processing governance milestone:
CC-23

Quality lifecycle milestone:
CC-28

Provincial baseline:
CC-33

Professional skillsets:
CC-34

Integration validation:
CC-35

Safety validation:
CC-36

Public readiness:
CC-38

v1 release decision:
CC-39
```

Final roadmap authority token:

```text
CANADIAN_CANNABIS_DEVELOPMENT_ROADMAP_V0_1_READY
```