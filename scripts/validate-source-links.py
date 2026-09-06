"""Validate AgentCannabis source registry URL metadata.

This is a deterministic metadata check. It does not fetch legal sources or prove
that a source is current at use.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    sources_dir = root / "sources"
    files = sorted(sources_dir.glob("*.json"))
    if not files:
        fail("No source registry files found")
    seen: set[str] = set()
    count = 0
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        records = data.get("sources")
        if not isinstance(records, list):
            fail(f"{path.relative_to(root)} sources must be a list")
        for source in records:
            count += 1
            source_id = source.get("id")
            if not isinstance(source_id, str) or not source_id:
                fail(f"{path.relative_to(root)} source missing id")
            if source_id in seen:
                fail(f"Duplicate source id: {source_id}")
            seen.add(source_id)
            url = source.get("source_url")
            if not isinstance(url, str):
                fail(f"{source_id} source_url must be a string")
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc:
                fail(f"{source_id} source_url must be an absolute https URL")
            if not source.get("targeted_claim"):
                fail(f"{source_id} missing targeted_claim")
            limitations = source.get("limitations")
            if not isinstance(limitations, list) or not limitations:
                fail(f"{source_id} must record limitations")
    print(json.dumps({"status": "PASS", "checked_sources": count}))


if __name__ == "__main__":
    main()
