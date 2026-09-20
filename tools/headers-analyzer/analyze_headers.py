#!/usr/bin/env python3
"""Defensive HTTP security-header analyzer.

Use only on websites you own or are authorized to assess.
The analyzer performs a normal HTTP request and evaluates response headers.
"""
from __future__ import annotations
import argparse
import json
import ssl
import sys
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Mapping

RECOMMENDED = {
    "content-security-policy": (
        "high",
        "Define a restrictive CSP appropriate to the application. Prefer nonces/hashes over unsafe-inline."
    ),
    "strict-transport-security": (
        "high",
        "For HTTPS-only production sites, consider HSTS after confirming all subdomains and preload implications."
    ),
    "x-content-type-options": (
        "medium",
        "Set X-Content-Type-Options: nosniff."
    ),
    "referrer-policy": (
        "medium",
        "Set an explicit Referrer-Policy based on privacy and application requirements."
    ),
    "permissions-policy": (
        "low",
        "Restrict browser capabilities that the application does not need."
    ),
}

@dataclass
class Finding:
    header: str
    severity: str
    status: str
    recommendation: str

def normalize(headers: Mapping[str, str]) -> dict[str, str]:
    return {str(k).strip().lower(): str(v).strip() for k, v in headers.items()}

def assess(headers: Mapping[str, str]) -> dict:
    h = normalize(headers)
    findings: list[Finding] = []
    for name, (severity, recommendation) in RECOMMENDED.items():
        if name in h and h[name]:
            findings.append(Finding(name, severity, "present", "Review value for application-specific correctness."))
        else:
            findings.append(Finding(name, severity, "missing", recommendation))

    clickjacking_ok = (
        "x-frame-options" in h
        or "frame-ancestors" in h.get("content-security-policy", "").lower()
    )
    findings.append(Finding(
        "clickjacking-protection",
        "medium",
        "present" if clickjacking_ok else "missing",
        "Use CSP frame-ancestors and/or X-Frame-Options where legacy compatibility is needed."
    ))

    server = h.get("server", "")
    powered = h.get("x-powered-by", "")
    info_disclosure = bool(server or powered)

    return {
        "summary": {
            "controls_checked": len(findings),
            "present": sum(f.status == "present" for f in findings),
            "missing": sum(f.status == "missing" for f in findings),
            "informational_technology_headers_present": info_disclosure,
        },
        "findings": [asdict(f) for f in findings],
        "observed": {
            "server": server or None,
            "x-powered-by": powered or None,
        },
    }

def fetch_headers(url: str, timeout: float = 8.0) -> tuple[str, dict[str, str]]:
    if not url.lower().startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "User-Agent": "MR-Security-Headers-Analyzer/1.0 (+defensive assessment)",
            "Range": "bytes=0-0",
            "Accept": "*/*",
        },
    )
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.geturl(), dict(resp.headers.items())

def load_headers(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Header JSON must be an object of name/value pairs.")
    return {str(k): str(v) for k, v in data.items()}

def main() -> int:
    p = argparse.ArgumentParser(description="Analyze defensive HTTP security headers.")
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--url", help="Authorized URL to analyze.")
    source.add_argument("--headers-json", type=Path, help="Offline JSON file containing response headers.")
    p.add_argument("--json", action="store_true", help="Print JSON output.")
    args = p.parse_args()

    try:
        if args.url:
            final_url, headers = fetch_headers(args.url)
        else:
            final_url, headers = "offline-sample", load_headers(args.headers_json)
        result = assess(headers)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({"target": final_url, **result}, indent=2))
        return 0

    print(f"Target: {final_url}")
    print(f"Present: {result['summary']['present']} | Missing: {result['summary']['missing']}")
    print("-" * 72)
    for finding in result["findings"]:
        mark = "OK" if finding["status"] == "present" else "REVIEW"
        print(f"[{mark:6}] {finding['header']} ({finding['severity']})")
        if finding["status"] != "present":
            print(f"         {finding['recommendation']}")
    if result["summary"]["informational_technology_headers_present"]:
        print("\n[INFO] Server technology headers were observed; decide whether they are necessary.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
