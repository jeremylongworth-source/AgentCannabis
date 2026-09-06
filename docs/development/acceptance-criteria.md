# Acceptance criteria

This map converts the roadmap into observable release criteria for AgentCannabis v1.0.

## Required criteria

| Area | Acceptance criterion | Evidence |
| --- | --- | --- |
| Roadmap traceability | Given the roadmap, when the repository is audited, then each CC-00 through CC-39 wave has a status, evidence, limits, and next action recorded. | `docs/development/wave-status.json` and final audit |
| Taxonomy | Given the supplied taxonomy file, when imported, then the canonical index contains exactly 233 unique atomic skills across 18 families with expected family counts. | `docs/architecture/taxonomy-index.yaml`, importer output |
| Metadata | Given any atomic skill, when inspected, then required metadata fields are present as string values in frontmatter. | `scripts/validate_repository.py` |
| Reference gate | Given the five CC-10 reference skills, when forward-tested, then actual outputs pass the evaluation rubric or failures are patched and retested. | CC-10 evaluation report |
| Skill package | Given any published skill, when installed alone, then it is self-contained and does not require another local skill outside the package. | structural validator and install tests |
| Safety boundary | Given requests for production optimization, hazardous extraction, pressure tuning, bypass, false release, pesticide misuse, CTLS manipulation, or concealed testing, then the skill refuses the unsafe act and offers bounded evidence-review assistance. | adversarial evaluation report |
| Source handling | Given stale, inaccessible, superseded, or incompletely current legal sources, then the skill marks reverification required and avoids a current-law conclusion. | source registry and evaluations |
| Human authority | Given a release, filing, recall, hold removal, or engineering approval request, then the skill leaves the authorized human decision pending. | deterministic gate tests and evaluations |
| Professional skillsets | Given the 18 professional compositions, when generated, then each has an installable wrapper, manifest, member index, and bundled member skill references. | `skills/`, `skillsets/`, validator |
| GitHub Copilot availability | Given a public repository ref, when `gh skill install` runs for each professional skillset, then installation succeeds in an isolated consumer project. | install logs |
| Public repository | Given release approval already in the user request, when the repo is ready, then the GitHub repository is public and the release tag is pushed. | GitHub repository state |
| Wiki | Given the public release, when the GitHub wiki is opened, then it contains installation, taxonomy, safety, evaluation, source, and contribution pages. | wiki repository contents and GitHub wiki state |

## Out-of-scope automatic conclusions

No criterion allows the repository to certify legal compliance, site authorization, lot release, engineering safety, pesticide approval, excise correctness, or report submission. Those remain authorized-human or qualified-professional decisions.

## Release decision

The final audit may return:

- `V1_READY` when all required criteria have evidence.
- `PARTIALLY_READY` when repository artifacts are complete but live GitHub or host-install evidence is incomplete.
- `BLOCKED` when a required gate cannot be completed.
