# Evaluation

AgentCannabis uses layered validation and evaluation. Structural checks, scenario specifications, actual forward tests, adversarial tests, and install tests are kept separate.

## Local validation

Run the release gate from the repository root:

```powershell
.\scripts\validate-all.ps1
```

The wrapper runs `python scripts/validate_repository.py --stage full`, `python scripts/validate-source-links.py --repo-root .`, and `python -m unittest discover -s tests -v`.

## Behavioral evidence

Evaluation reports live under `docs/development/evaluations/`:

- `CC-10-forward-test.md`: five reference skills and captured output review
- `CC-35-integrated-workflows.md`: integrated workflow cases and scoring
- `CC-36-adversarial-evaluations.md`: adversarial boundary cases and scoring

Scenario files inside skill packages are specifications. They are not execution evidence until outputs are captured, scored, fixed where needed, and retested.

## Install evidence

The public release gate verifies all 18 professional skillsets with `gh skill install` from a release tag. Install success proves packaging availability, not legal correctness or future model behavior.

Release `v1.0.3` validates the structural repository, source records, deterministic review gate, root routing templates, GitHub skill packaging dry run, and all 18 public professional skillset installs.
