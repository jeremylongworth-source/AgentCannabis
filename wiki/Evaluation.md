# Evaluation

AgentCannabis keeps different kinds of evidence separate. A validator can
prove repository structure, an install check can prove package availability,
and a captured evaluation can show how a bounded workflow behaved on a given
fixture. None of these alone proves current law, site applicability, or
professional approval.

## Local validation

Run the release gate from the repository root:

```powershell
.\scripts\validate-all.ps1
```

The wrapper runs structural validation, source-link validation, and the
deterministic review-gate test suite. Preview public package metadata with:

```powershell
.\scripts\publish_skill_repository.ps1 -DryRun
```

## Behavioral evidence

Evaluation reports live under `docs/development/evaluations/`:

- `CC-10-forward-test.md` — five reference skills and captured output review;
- `CC-35-integrated-workflows.md` — integrated workflow cases and scoring; and
- `CC-36-adversarial-evaluations.md` — adversarial boundary cases and scoring.

Scenario files inside skill packages are specifications. They are not execution
evidence until outputs are captured, scored, fixed where needed, and retested.
The reports describe their fixture scope, reviewer method, and limitations.

## Install evidence

The public release gate verifies all 18 professional skillsets with
`gh skill install` from a release tag in fresh destination projects. Install
success proves packaging availability and discoverability; it does not prove
legal correctness, current source applicability, or future model behavior.

Release `v1.0.5` records passing structural validation, source records,
deterministic review gates, root routing templates, GitHub skill packaging dry
run, and all 18 public professional skillset installs.

## Reading an evaluation result

When reviewing a report, check:

1. whether the fixture is fictional and the inputs are complete;
2. which sources were available and what dates or applicability limits they
   carried;
3. whether the output preserved unknowns and escalated regulated or hazardous
   decisions; and
4. whether the result was reproduced after a fix.
