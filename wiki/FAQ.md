# FAQ

## Is AgentCannabis only for GitHub Copilot?

No. Copilot is a supported install target, but the repository also contains
portable skill folders and root `agents/AGENTS.*.md` routing templates for
local agent hosts. GitHub CLI currently supports several Agent Skills hosts;
choose the host value supported by your installed CLI.

## Which release should I install?

Use `v1.0.5` for stable, reproducible installs. Use `main` only when you
deliberately want the latest development state. Preview a release before
installing it.

## Should I install all 233 atomic skills?

Usually no. Start with one professional skillset. Its wrapper includes a
member index and bundled references for role-level routing. Install an atomic
skill separately when the task is narrow or you want direct discovery.

## What is the difference between an atomic skill and a professional wrapper?

An atomic skill handles one bounded workflow. A professional wrapper composes
existing atomic skills for a role and carries the routing metadata needed to
select among them. The wrapper does not add new authority or hidden procedures.

## Can AgentCannabis approve a lot release or regulatory filing?

No. It can organize evidence and prepare a review package, but the responsible
authorized human or qualified professional must make the regulated decision.

## Are the source snapshots current law?

No. They are dated source records with stated limits. Current primary-source
verification and actual site evidence are required before site-specific legal,
tax, quality, engineering, filing, or operational conclusions.

## Why are many atomic skills regular in structure?

The v1 taxonomy is broad. Generated structure keeps metadata, references,
boundaries, and validation consistent. Future depth should be driven by
reviewed usage evidence rather than by silently changing the taxonomy.

## Why are skillset manifests JSON instead of AgentSkills YAML?

AgentCannabis uses JSON manifests because its generators and validators consume
`skillsets/<name>.json`. The installable runtime packages use the standard
`skills/<name>/SKILL.md` shape, and the repository provides AgentSkills-style
routing templates under `agents/`.

## Why use `publish_skill_repository.ps1` for dry runs?

Some Windows checkouts have `.git` ownership that differs from the interactive
user. GitHub CLI can then emit a false `not a git repository` warning during
`gh skill publish`, even when the dry run succeeds. The wrapper scopes
`safe.directory` to that process instead of changing global Git configuration.

## Does a passing install prove the skill is safe or legally correct?

No. An install check proves that the public package can be retrieved and
placed in a host location. Structural and evaluation evidence still has scope
and currentness limits, and regulated work requires qualified human review.
