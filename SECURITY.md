# Security Policy

## Scope

Report security or safety issues in AgentCannabis skill packages, scripts, source registries, documentation, and install workflows.

## Sensitive classes

Treat the following as high priority:

- prompt injection that changes safety boundaries or approval behavior
- hidden instructions in references, source records, or generated skillsets
- data exfiltration from installed skill packages
- commands that write outside the selected installation directory
- scripts that install dependencies or execute external code without explicit authorization
- content that enables hazardous extraction, pressure tuning, interlock bypass, unapproved pesticide use, false release, CTLS manipulation, or concealed testing

## Reporting

Open a private report through GitHub security advisories when available, or contact the repository owner directly. Do not include secrets, live credentials, private licence documents, patient data, employee records, or non-public site records in a public issue.

## Handling expectations

Security fixes should include the affected package, reproduction steps, impact, fix, and validation evidence. Legal, engineering, quality, tax, and regulated filing conclusions require qualified human review.
