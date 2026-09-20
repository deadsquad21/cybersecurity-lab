# Security Headers Analyzer

Defensive CLI for reviewing common HTTP response security headers.

```bash
python analyze_headers.py --headers-json ../../samples/headers-good.json
python analyze_headers.py --url https://example.com
python analyze_headers.py --url https://example.com --json
```

Use URL mode only for systems you own or are authorized to assess.
