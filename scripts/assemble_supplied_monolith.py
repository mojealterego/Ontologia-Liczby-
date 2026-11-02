#!/usr/bin/env python3
"""Append verified supplements to the supplied 629-page book without changing its pages.

This is explicitly NOT canonical release 0.20 (864 pages). No final TOC is made.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import fitz

BASE_SHA256 = 'cd2e5e9ef0adefc3344ff8a7a1bcaa4befd2e1b85b4a711a36c3a0c179cb1309'
BASE_PAGES = 629
MAX_BYTES = 99_000_000
CHECK_RENDER_PAGES = (0, 1, 32, 33, 628)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for part in iter(lambda: f.read(1024 * 1024), b''):
            h.update(part)
    return h.hexdigest()


def text_sha(page) -> str:
    return hashlib.sha256(page.get_text().encode('utf-8')).hexdigest()


def render_sha(page) -> str:
    return hashlib.sha256(page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False).samples).hexdigest()


def assemble(base: Path, chapters: list[Path], output: Path, manifest: Path) -> dict:
    if len(chapters) != 2:
        raise ValueError('Exactly two supplements (97C20 and 97C30) are required')
    inputs = [base, *chapters]
    if any(not p.is_file() for p in inputs):
        raise FileNotFoundError('Input PDF missing')
    if len({p.resolve() for p in inputs}) != len(inputs):
        raise ValueError('Duplicate input PDF')
    if output.resolve() in {p.resolve() for p in inputs} or manifest.resolve() in {p.resolve() for p in inputs}:
        raise ValueError('Refusing to overwrite input')
    if output.resolve() == manifest.resolve():
        raise ValueError('Output and manifest must differ')
    if sha256(base) != BASE_SHA256:
        raise ValueError('Supplied base PDF hash mismatch: not the verified 629-page source')
    with fitz.open(base) as original:
        if len(original) != BASE_PAGES:
            raise ValueError('Supplied base PDF page count mismatch')
        for marker in ('97C20', '97C30'):
            if any(marker in page.get_text() for page in original):
                raise ValueError(f'Chapter marker {marker} already exists in base')
        old_text = [text_sha(page) for page in original]
        old_render = {i: render_sha(original[i]) for i in CHECK_RENDER_PAGES}
        combined = fitz.open()
        combined.insert_pdf(original, links=True, annots=True)
        supplements = []
        for marker, path in zip(('97C20', '97C30'), chapters):
            with fitz.open(path) as chapter:
                if not len(chapter) or any(not p.get_text().strip() for p in chapter):
                    raise ValueError(f'Blank chapter: {path}')
                if marker not in ''.join(p.get_text() for p in chapter):
                    raise ValueError(f'Wrong chapter for {marker}: {path}')
                combined.insert_pdf(chapter)
                supplements.append({'marker': marker, 'sha256': sha256(path), 'pages': len(chapter)})
        combined.set_metadata({'title': 'ONTOLOGIA LICZBY — Tom I — robocza integracja 629 + suplementy',
                               'author': 'Andrzej Mikulski',
                               'subject': 'Niekanoniczny podglad; bez koncowego spisu tresci'})
        output.parent.mkdir(parents=True, exist_ok=True)
        combined.save(output, garbage=3, deflate=True)
        combined.close()
    if output.stat().st_size >= MAX_BYTES:
        output.unlink(missing_ok=True)
        raise ValueError('PDF exceeds strict 99 MB limit')
    with fitz.open(output) as verified:
        if len(verified) != BASE_PAGES + sum(x['pages'] for x in supplements):
            raise ValueError('Unexpected page count')
        if any(text_sha(verified[i]) != old_text[i] for i in range(BASE_PAGES)):
            raise ValueError('Original page text changed')
        if any(render_sha(verified[i]) != old_render[i] for i in CHECK_RENDER_PAGES):
            raise ValueError('Original page rendering changed')
        result = {'status': 'verified_noncanonical_preview', 'canonical_0_20_verified': False,
                  'base_sha256': BASE_SHA256, 'base_pages_preserved': BASE_PAGES,
                  'sampled_original_render_pages': [i + 1 for i in CHECK_RENDER_PAGES],
                  'supplements': supplements, 'result_pages': len(verified),
                  'historical_scientific_pages': 585, 'canonical_pages_added': 0,
                  'final_table_of_contents_created': False, 'bytes': output.stat().st_size,
                  'sha256': sha256(output)}
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return result


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base', type=Path, required=True)
    p.add_argument('--chapter', type=Path, action='append', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--manifest', type=Path, required=True)
    args = p.parse_args()
    print(json.dumps(assemble(args.base, args.chapter, args.output, args.manifest), ensure_ascii=False))


if __name__ == '__main__':
    main()
