# Web Application Assessment Methodology

## 1. Scope & Authorization
Document approved hosts, applications, accounts, test windows, excluded actions, and escalation contacts.

## 2. Architecture Understanding
Map the application at a high level: browser, reverse proxy/CDN, application layer, identity provider, APIs, storage, and external integrations.

## 3. Baseline Review
Review TLS use, HTTP headers, cookie attributes, authentication flows, session behavior, error handling, and publicly exposed configuration.

## 4. Control Validation
Validate security controls in a non-destructive manner. Prefer test accounts and synthetic data.

## 5. Findings
For each finding record:
- title
- environment
- evidence
- security impact
- affected control
- remediation
- retest status

## 6. Retest
Confirm the remediation fixed the observed weakness without creating a regression.

## 7. Publication
Only publish sanitized lab material or material explicitly approved for public release.
