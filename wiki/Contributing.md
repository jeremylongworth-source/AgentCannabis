# Contributing

Contributions must preserve the frozen taxonomy, self-contained skill packages, and safety boundaries.

Before changing skills, run:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_repository.py --stage reference
gh skill publish D:\AgentCannabis --dry-run
```

Before release, run full validation after all atomic and professional skillset packages exist:

```powershell
python scripts/validate_repository.py --stage full
```

Do not add unsafe operational instructions or mark a roadmap wave ready without evidence.
