# Skill authoring standard

The supplied v1 taxonomy is the authority for atomic names and family membership. A folder at `skills/<name>/SKILL.md` is the installation unit. Professional compositions are additional packages and must not inflate the 233-atomic count.

Every entrypoint uses Agent Skills frontmatter with `name`, `description`, and string-valued `metadata` for family, tier, production_stage, jurisdiction, licence_dependency, responsible_role, regulatory_sensitivity, hazard_class, human_approval_required and source_freshness. Package-kind metadata distinguishes atomic and professional skillset packages.

Every skill contains triggers, non-triggers, inputs, assumptions, dependencies, licence requirements, responsible role, a task-specific review procedure, evidence and source requirements, hazard behavior, outputs, limitations, human approval and test references. Required headings are structural checks; useful domain-specific decision criteria are assessed separately.

Skills must install independently: every local reference needed at runtime is contained within that skill folder. Shared authoring material may be generated into packages; a consistency check must detect drift. References copied into skillset bundles retain source attribution and relative-link integrity.

Descriptions distinguish similar tasks (for example a COA review from lot-release readiness). Do not embed secrets, real producer fixtures, scraped manuals, current pesticide lists, unsupported legal deadlines or universal production recipes. Keep operational cultivation/production, potency optimization and hazardous equipment procedures outside the supported assistance; use evidence-review and governance outputs.

Write realistic positive, negative, routing, freshness and human-authority scenarios before closing each skill's development gate. Record what was actually executed and what remains a scenario specification. Do not label generated expected text as model evaluation results.
