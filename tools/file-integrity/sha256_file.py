#!/usr/bin/env python3
from pathlib import Path
import argparse
import hashlib

def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    p = argparse.ArgumentParser(description="Calculate SHA-256 for a local file.")
    p.add_argument("path", type=Path)
    args = p.parse_args()
    print(sha256_file(args.path))

if __name__ == "__main__":
    main()
