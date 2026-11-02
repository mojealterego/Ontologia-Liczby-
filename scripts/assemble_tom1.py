#!/usr/bin/env python3
"""Build a traceable, noncanonical working Tom I PDF from existing chapter PDFs.

Two explicit modes:
- supplements: continuous working corpus of new chapters, without claiming the historic preface.
- with-base: verified 0.20 (864 pages, SHA256 pinned) + supplements, preserving pages 1-33.

Never creates a final table of contents or edits input files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

CANONICAL_SHA256 = "ea888d112cc255856c03cead7428d4f817ad2c692d0e6e6d61f46ae17738dd43"
CANONICAL_PAGES = 864
HISTORICAL_PREFACE_PAGES = 33
MAX_BYTES = 99_000_000


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def page_text_digest(page) -> str:
    return hashlib.sha256((page.extract_text() or "").encode("utf-8")).hexdigest()


def build(mode: str, base: Path | None, chapters: list[Path], output: Path, manifest: Path) -> dict:
    if mode not in {"supplements", "with-base"}:
        raise ValueError("Unsupported mode")
    if not chapters:
        raise ValueError("At least one chapter PDF is required")
    if output.resolve() == manifest.resolve():
        raise ValueError("Output and manifest must be distinct")
    inputs = chapters + ([base] if base is not None else [])
    if any(path is None or not path.is_file() for path in inputs):
        raise FileNotFoundError("Missing input PDF")
    if len({p.resolve() for p in inputs}) != len(inputs):
        raise ValueError("Duplicate input PDFs are not allowed")
    if any(p.resolve() in {output.resolve(), manifest.resolve()} for p in inputs):
        raise ValueError("Output cannot overwrite an input")
    if mode == "with-base" and base is None:
        raise ValueError("with-base requires --base")
    if mode == "supplements" and base is not None:
        raise ValueError("supplements mode forbids --base")

    writer = PdfWriter()
    source_manifest = []
    history_digests = []
    if base is not None:
        actual_hash = sha256_file(base)
        if actual_hash != CANONICAL_SHA256:
            raise ValueError(f"Original 0.20 SHA256 mismatch: {actual_hash}")
        reader = PdfReader(str(base), strict=True)
        if len(reader.pages) != CANONICAL_PAGES:
            raise ValueError(f"Original 0.20 must have {CANONICAL_PAGES} pages")
        history_digests = [page_text_digest(reader.pages[i]) for i in range(HISTORICAL_PREFACE_PAGES)]
        writer.append(reader)
        source_manifest.append({"kind": "original_0.20", "path": str(base), "sha256": actual_hash, "pages": len(reader.pages)})

    for chapter in chapters:
        reader = PdfReader(str(chapter), strict=True)
        if len(reader.pages) == 0:
            raise ValueError(f"Empty PDF: {chapter}")
        if any(not (page.extract_text() or "").strip() for page in reader.pages):
            raise ValueError(f"Blank/textless page in {chapter}")
        writer.append(reader)
        source_manifest.append({"kind": "supplement", "path": str(chapter), "sha256": sha256_file(chapter), "pages": len(reader.pages)})

    writer.add_metadata({
        "/Title": "Ontologia Liczby — Tom I — wydanie robocze, niekanoniczne",
        "/Author": "Andrzej Mikulski",
        "/Subject": "Zeszyt zintegrowanych rozdzialow; bez koncowego spisu tresci",
    })
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as out:
        writer.write(out)
    bytes_written = output.stat().st_size
    if bytes_written >= MAX_BYTES:
        output.unlink(missing_ok=True)
        raise ValueError(f"Output exceeds strict size limit: {bytes_written} bytes")

    verification = PdfReader(str(output), strict=True)
    total_expected = sum(item["pages"] for item in source_manifest)
    if len(verification.pages) != total_expected:
        output.unlink(missing_ok=True)
        raise ValueError("Page count changed during assembly")
    if history_digests:
        for i, original_digest in enumerate(history_digests):
            if page_text_digest(verification.pages[i]) != original_digest:
                output.unlink(missing_ok=True)
                raise ValueError(f"Historical preface text changed on page {i + 1}")

    result = {
        "status": "verified_working_corpus_not_final_tom_i",
        "mode": mode,
        "original_0_20_verified": bool(base),
        "historical_preface_text_pages_checked": len(history_digests),
        "final_table_of_contents_created": False,
        "historical_scientific_page_count": 585,
        "scientific_pages_added_to_canonical_count": 0,
        "page_count": len(verification.pages),
        "byte_count": bytes_written,
        "size_limit_exclusive": MAX_BYTES,
        "sha256": sha256_file(output),
        "sources": source_manifest,
    }
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=["supplements", "with-base"])
    parser.add_argument("--base", type=Path)
    parser.add_argument("--chapter", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(args.mode, args.base, args.chapter, args.output, args.manifest)
    except (ValueError, FileNotFoundError, OSError) as exc:
        print(f"Assembly rejected: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({k: v for k, v in result.items() if k != "sources"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
