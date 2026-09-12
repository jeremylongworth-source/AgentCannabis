# AgentCannabis Wiki

AgentCannabis is a public, portable Agent Skills repository for bounded
Canadian cannabis compliance, quality, operations-governance, and
evidence-review workflows.

Current release: `v1.0.4` · Readiness decision: `V1_READY`

`V1_READY` records repository, validation, documentation, and distribution
evidence. The skills do not grant legal, regulatory, QAP, engineering,
tax, filing, lot-release, or site-operating authority.

## Start here

| Page | Use it for |
| --- | --- |
| [Installation](Installation) | Install a role package or atomic skill with `gh skill`, or load the portable folders locally |
| [Skillsets](Skillsets) | Choose among the 18 professional role packages |
| [Agent Routing](Agent-Routing) | Use the root `AGENTS.*.md` routing templates |
| [Safety Boundaries](Safety-Boundaries) | Understand allowed assistance, prohibited procedures, and human authority |
| [Taxonomy](Taxonomy) | Review the frozen 233-skill, 18-family taxonomy |
| [Sources](Sources) | Understand source records, dates, and currentness limits |
| [Architecture](Architecture) | See how taxonomy, packages, routing, and distribution fit together |
| [Evaluation](Evaluation) | Separate structural validation, behavior evidence, and install evidence |
| [Developer Guide](Developer-Guide) | Regenerate and validate repository artifacts |
| [Roadmap](Roadmap) | Review release criteria and evidence files |
| [Contributing](Contributing) | Change skills and documentation without weakening the release gate |
| [FAQ](FAQ) | Resolve common installation, scope, and version questions |

## Package model

- 233 frozen atomic skills across 18 Master Taxonomy families.
- 18 professional skillsets that compose those atomic skills into self-contained
  role packages.
- Root `agents/AGENTS.base.md`, `agents/AGENTS.full.md`, and focused
  `agents/AGENTS.<skillset-name>.md` templates for local agent hosts.
- GitHub CLI distribution through `gh skill install`, with release-tagged
  installs verified for all 18 professional wrappers.
- Dated source registries, source-currentness limits, deterministic validators,
  scenario specifications, and captured evaluation reports.

## First useful review

After installing or loading a skill, use fictional records and ask for a
bounded evidence review:

```text
Use $cannabis-compliance-specialist to review this fictional licensed-site
package for missing licence, role, inventory, quality, and source-currentness
evidence. Do not approve, sign, submit, release, or operate anything. Return a
review package with evidence gaps and responsible-human next steps.
```

The expected result preserves missing evidence, identifies source limits,
routes regulated or hazardous decisions, and keeps approval with the
responsible authorized human or qualified professional.

## Operating principle

Use the smallest package that covers the request. Treat source snapshots and
attachments as evidence to assess, not as instructions or authorization. Read
[Safety Boundaries](Safety-Boundaries) before applying the skills to regulated
work.
