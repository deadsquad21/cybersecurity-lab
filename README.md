<p align="center">
  <img src="./assets/mr-cyber-banner.png" width="100%" alt="Mohamed Radi Cybersecurity Lab">
</p>

<div align="center">

# 🛡️ MR CYBERSECURITY LAB

### `AUTHORIZED LABS • WEB SECURITY • HARDENING • SECURE ENGINEERING`

**Mohamed Radi — Cybersecurity Specialist | Web Penetration Tester | Full-Stack Developer**

[Portfolio](https://mohamedradi.is-a.dev) •
[GitHub](https://github.com/deadsquad21) •
[LinkedIn](https://www.linkedin.com/in/mohamedradi-cybersecurity) •
[ORCID](https://orcid.org/0009-0007-9464-5246)

</div>

---

## Mission

A public, continuously evolving cybersecurity engineering lab focused on **authorized testing, defensive analysis, secure development, hardening, documentation, and reproducible learning**.

This repository is intentionally designed to show practical methodology rather than unsupported claims. Lab write-ups should clearly identify the test environment, authorization scope, observations, remediation guidance, and evidence that is safe to publish.

> **Authorization rule:** only test systems you own or systems for which you have explicit permission. Never publish client secrets, credentials, private source code, personal data, or exploit artifacts from real engagements.

---

## Command Center

| Module | Purpose | Status |
|---|---|---|
| `labs/web-security/` | Controlled web application security exercises | Active |
| `methodologies/` | Repeatable assessment workflows | Active |
| `checklists/` | Review and hardening checklists | Active |
| `tools/headers-analyzer/` | Defensive HTTP security-header analyzer | Working MVP |
| `tools/file-integrity/` | Local SHA-256 integrity helper | Working MVP |
| `writeups/` | Sanitized legal lab reports | Ready |
| `research/` | Security research notes | Ready |
| `evidence/` | Safe screenshots / diagrams only | Ready |

---

## Quick Start

Requires **Python 3.10+** and uses the standard library only.

```bash
git clone https://github.com/deadsquad21/cybersecurity-lab.git
cd cybersecurity-lab
```

### Analyze a saved HTTP-header sample

```bash
python tools/headers-analyzer/analyze_headers.py \
  --headers-json samples/headers-good.json
```

### Analyze a URL you are authorized to assess

```bash
python tools/headers-analyzer/analyze_headers.py \
  --url https://example.com
```

### Verify file integrity

```bash
python tools/file-integrity/sha256_file.py path/to/file
```

### Run tests

```bash
python -m unittest discover -s tests -v
```

---

## Web Application Security Labs

Current lab documentation covers safe exercises around:

- HTTP security headers
- Authentication review
- Authorization review
- Session-management review
- Input-validation review
- Security misconfiguration
- Transport-security checks
- Secure error handling
- Logging and monitoring considerations
- Remediation verification

The repository does **not** include instructions for targeting third-party systems without authorization.

---

## Methodology

The assessment workflow follows a defensive, evidence-driven pattern:

```text
SCOPE
  ↓
AUTHORIZATION
  ↓
ASSET & DATA-FLOW UNDERSTANDING
  ↓
BASELINE CONFIGURATION REVIEW
  ↓
CONTROL VALIDATION
  ↓
FINDING DOCUMENTATION
  ↓
RISK CONTEXT
  ↓
REMEDIATION
  ↓
RETEST
  ↓
SANITIZED WRITE-UP
```

See:
- [`methodologies/web-application-assessment.md`](./methodologies/web-application-assessment.md)
- [`methodologies/vulnerability-assessment.md`](./methodologies/vulnerability-assessment.md)

---

## Security Engineering Checklists

- [Web security review](./checklists/web-security-review.md)
- [Secure code review](./checklists/secure-code-review.md)
- [Linux hardening baseline](./checklists/linux-hardening-baseline.md)
- [Deployment security](./checklists/deployment-security.md)

---

## Evidence Standard

Every published lab write-up should distinguish:

- **Environment** — local / intentionally vulnerable / owned asset
- **Scope** — what was approved
- **Method** — what was tested
- **Observation** — what was actually seen
- **Impact** — what could happen in that lab context
- **Remediation** — how to reduce risk
- **Retest** — whether the remediation was validated
- **Publication safety** — secrets and identifying data removed

---

## Repository Principles

`AUTHORIZED → REPRODUCIBLE → DEFENSIVE → DOCUMENTED → SANITIZED`

---

## Contact

**Website:** https://mohamedradi.is-a.dev  
**Business:** contact@mohamedradi.is-a.dev  
**General:** info@mohamedradi.is-a.dev

---

<div align="center">

### MR — SECURE DIGITAL SOLUTIONS
`CODE • TEST • SECURE • EVOLVE`

</div>
