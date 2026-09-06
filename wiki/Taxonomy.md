# Taxonomy

Master Taxonomy v1.0 is frozen at 233 unique atomic skills across 18 families.

The canonical machine-readable index is `docs/architecture/taxonomy-index.yaml`. The extension is `.yaml`, but the file content is JSON-compatible and is validated by repository scripts.

## Family map

| Family | Name | Count | Example skill |
| --- | --- | ---: | --- |
| 01 | Regulatory, Licensing & Authorized Activities | 12 | `classify-cannabis-business-activity` |
| 02 | Site Roles, Security & Facility Governance | 10 | `identify-required-site-roles` |
| 03 | Genetics, Starting Material & Propagation | 12 | `review-starting-material-provenance` |
| 04 | Cultivation Systems & Crop Planning | 12 | `classify-cultivation-system` |
| 05 | Environmental & Controlled-Growing Systems | 13 | `build-environment-monitoring-plan` |
| 06 | Root Zone, Irrigation & Crop Inputs | 12 | `classify-growing-medium` |
| 07 | Plant Health, Pest & Disease Management | 13 | `build-plant-health-monitoring-plan` |
| 08 | Crop Management, Monitoring & Harvest | 12 | `build-crop-monitoring-plan` |
| 09 | Post-Harvest Intake, Handling & Trimming | 10 | `plan-post-harvest-material-flow` |
| 10 | Drying, Curing, Storage & Stability | 13 | `build-drying-monitoring-plan` |
| 11 | Processing & Refinement Governance | 12 | `classify-cannabis-processing-method` |
| 12 | Hazardous Processing & Preventive Controls | 12 | `classify-processing-hazard` |
| 13 | GPP, Sanitation & Quality Systems | 23 | `draft-cannabis-sop` |
| 14 | Laboratory Testing & Quality Assurance | 16 | `build-cannabis-sampling-plan` |
| 15 | Product Classification, Formulation & Packaging | 14 | `classify-cannabis-product` |
| 16 | Inventory, Lot Lineage, CTLS & Excise | 16 | `reconcile-cannabis-inventory` |
| 17 | Complaints, Recalls & Post-Market Surveillance | 11 | `triage-cannabis-quality-complaint` |
| 18 | Safety, Compliance Audit & Continuous Improvement | 10 | `identify-cannabis-workplace-hazard` |

## Skill metadata

Every atomic skill records family, tier, production stage, jurisdiction, licence dependency, responsible role, regulatory sensitivity, hazard class, human approval requirement, source freshness requirement, and package kind.

## Alias handling

`identify-responsible-role` is an alias, not an atomic skill. It resolves to `identify-required-site-roles` and `map-site-role-responsibilities`.

Taxonomy import must preserve exactly 233 atomic skills and the family counts above.
