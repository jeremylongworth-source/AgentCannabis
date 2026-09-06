# Taxonomy

Master Taxonomy v1.0 is frozen at 233 unique atomic skills across 18 families.

The canonical machine-readable index is `docs/architecture/taxonomy-index.yaml`. It records the family, tier, production stage, jurisdiction, licence dependency, responsible role, regulatory sensitivity, hazard class, human approval requirement, and source-freshness requirement for every atomic skill.

The alias `identify-responsible-role` is not an atomic skill. It resolves to:

- `identify-required-site-roles`
- `map-site-role-responsibilities`

Taxonomy import must preserve the exact 233-skill count and family counts.
