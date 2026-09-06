# Architecture

AgentCannabis is built around three layers: taxonomy, skill packages, and routing/distribution.

## Taxonomy layer

The Master Taxonomy v1.0 defines 233 atomic skills across 18 families. It is frozen for v1.0, and validators enforce the count, unique names, metadata fields, and family counts.

## Skill package layer

Every installable skill lives under `skills/<name>/` and contains its own runtime material. Atomic skills and professional wrappers share the same package shape: `SKILL.md`, `agents/openai.yaml`, `references/review-contract.md`, `references/sources.json`, and `references/scenarios.json`.

Professional wrappers also include `references/member-index.json`, which lists included atomic workflows and their metadata.

## Routing layer

The root `agents/` directory provides AgentSkills-style routing templates for local agent hosts. These templates route broad requests to professional skillsets and narrow requests to atomic skills where available.

## Distribution layer

GitHub Copilot installation is supported through `gh skill install`. Release-tagged installs use the self-contained professional wrappers under `skills/<skillset-name>/`.

## Review model

AgentCannabis does not convert agent output into regulatory authority. Its architecture keeps review assistance separate from human approvals, qualified professional decisions, source-currentness verification, and operational execution.
