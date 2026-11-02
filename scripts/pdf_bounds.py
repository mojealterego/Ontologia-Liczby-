#!/usr/bin/env python3
"""Check PDF word bounds and optionally apply minimal page-content scaling.

The original Markdown and page media boxes remain unchanged. Repair only pages
whose extracted word boxes extend beyond the requested safety inset.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import fitz
from pypdf import PdfReader, PdfWriter, Transformation


def out_of_bounds(path: Path, inset: float = 5.0) -> dict[int, int]:
    result: dict[int, int] = {}
    with fitz.open(path) as doc:
        for i, page in enumerate(doc):
            r = page.rect
            n = sum(1 for w in page.get_text('words')
                    if w[0] < inset or w[1] < inset
                    or w[2] > r.width - inset or w[3] > r.height - inset)
            if n:
                result[i] = n
    return result


def repair(path: Path, inset: float = 5.0, scale: float = 0.98) -> dict[int, int]:
    if not (0.9 <= scale < 1):
        raise ValueError('scale must be in [0.9, 1)')
    for _ in range(3):
        bad = out_of_bounds(path, inset)
        if not bad:
            return {}
        reader = PdfReader(str(path))
        writer = PdfWriter()
        for i, page in enumerate(reader.pages):
            if i in bad:
                w, h = float(page.mediabox.width), float(page.mediabox.height)
                page.add_transformation(Transformation().scale(scale).translate(w*(1-scale)/2, h*(1-scale)/2))
            writer.add_page(page)
        with NamedTemporaryFile(mode='wb', suffix='.pdf', dir=path.parent, delete=False) as tmp:
            tmp_name = tmp.name
            writer.write(tmp)
        os.replace(tmp_name, path)
    remaining = out_of_bounds(path, inset)
    if remaining:
        raise RuntimeError(f'PDF still has out-of-page text: {remaining}')
    return {}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf', type=Path)
    ap.add_argument('--repair', action='store_true')
    ap.add_argument('--inset', type=float, default=5.0)
    args = ap.parse_args()
    if not args.pdf.is_file():
        ap.error('PDF not found')
    before = out_of_bounds(args.pdf, args.inset)
    if before and args.repair:
        repair(args.pdf, args.inset)
    after = out_of_bounds(args.pdf, args.inset)
    print(f'pages_with_outliers_before={len(before)} after={len(after)}; words_before={sum(before.values())} words_after={sum(after.values())}')
    if after:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
