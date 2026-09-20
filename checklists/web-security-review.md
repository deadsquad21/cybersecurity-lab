# Web Security Review Checklist

## Transport
- [ ] HTTPS enforced
- [ ] Mixed content avoided
- [ ] HSTS considered for HTTPS-only deployments

## Headers
- [ ] Content-Security-Policy
- [ ] X-Content-Type-Options
- [ ] Referrer-Policy
- [ ] Permissions-Policy
- [ ] Clickjacking protection through CSP `frame-ancestors` or X-Frame-Options

## Authentication
- [ ] Passwords are hashed with a modern password-hashing function
- [ ] Login responses do not reveal unnecessary account state
- [ ] Rate limiting / abuse controls considered
- [ ] MFA supported where risk warrants it

## Sessions
- [ ] Cookies use HttpOnly where appropriate
- [ ] Cookies use Secure over HTTPS
- [ ] SameSite selected intentionally
- [ ] Session rotation on authentication
- [ ] Logout invalidates session state

## Input / Output
- [ ] Server-side validation
- [ ] Context-aware output encoding
- [ ] Parameterized database queries
- [ ] File uploads constrained and isolated

## Operations
- [ ] Sensitive data excluded from logs
- [ ] Security-relevant events logged
- [ ] Dependencies reviewed
- [ ] Secrets kept out of source control
