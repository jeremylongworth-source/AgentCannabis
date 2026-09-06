# FAQ

## Is AgentCannabis only for GitHub Copilot?

No. Copilot install is supported, but AgentCannabis also includes portable skill folders and root `agents/AGENTS.*.md` routing templates for local agent hosts.

## Which release should I install?

Use `v1.0.3` for stable installs. Use `main` only when you deliberately want the latest repository state.

## Do I need to install all 233 atomic skills?

Usually no. Start with one professional skillset. The wrapper includes a member index and bundled references for role-level routing. Install atomic skills separately only when you want direct invocation of narrow workflows.

## Can AgentCannabis approve a lot release or regulatory filing?

No. It can prepare a review package and identify gaps, but the responsible authorized human or qualified professional must make regulated decisions.

## Are the source snapshots current law?

No. They are dated source records with limitations. Current primary-source verification is required before site-specific conclusions.

## Why are many atomic skills regular in structure?

The v1.0 taxonomy is broad. Regular generated structure keeps boundaries, metadata, references, and validation consistent. Future releases can deepen high-use skills based on usage evidence.

## Why JSON skillset manifests instead of AgentSkills YAML manifests?

AgentCannabis uses JSON manifests because its generator and installer validate `skillsets/<name>.json`. The repository still provides AgentSkills-style routing behavior through root `agents/AGENTS.*.md` files.
