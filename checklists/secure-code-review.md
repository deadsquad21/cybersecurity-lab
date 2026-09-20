# Secure Code Review Checklist

- [ ] Trust boundaries identified
- [ ] Authentication and authorization checked independently
- [ ] User input validated server-side
- [ ] SQL/command execution uses safe APIs
- [ ] Output encoding matches rendering context
- [ ] Secrets are externalized
- [ ] Cryptographic functions use maintained libraries
- [ ] Error messages avoid sensitive details
- [ ] Logging avoids credentials/tokens
- [ ] Dependency versions are maintained
- [ ] Security-sensitive defaults are fail-closed
- [ ] Tests cover expected misuse cases
