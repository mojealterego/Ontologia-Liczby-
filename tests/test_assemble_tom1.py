"""Regression tests for strict Tom I working-book assembly."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas

from scripts.assemble_tom1 import CANONICAL_PAGES, MAX_BYTES, build, sha256_file


def sample_pdf(path: Path, label: str, pages: int = 1) -> None:
    canvas = Canvas(str(path), pagesize=A4)
    for n in range(pages):
        canvas.drawString(50, 790, f"{label} page {n + 1}")
        canvas.showPage()
    canvas.save()


class TomIAssemblyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.one = self.root / "chapter1.pdf"
        self.two = self.root / "chapter2.pdf"
        self.output = self.root / "book.pdf"
        self.manifest = self.root / "manifest.json"
        sample_pdf(self.one, "Chapter 1", 2)
        sample_pdf(self.two, "Chapter 2", 3)

    def tearDown(self):
        self.temp.cleanup()

    def test_supplements_merge_and_manifest(self):
        result = build("supplements", None, [self.one, self.two], self.output, self.manifest)
        self.assertEqual(result["page_count"], 5)
        self.assertEqual(result["scientific_pages_added_to_canonical_count"], 0)
        self.assertEqual(result["historical_preface_text_pages_checked"], 0)
        self.assertFalse(result["final_table_of_contents_created"])
        self.assertEqual(result["sha256"], sha256_file(self.output))
        self.assertEqual(json.loads(self.manifest.read_text())["sha256"], result["sha256"])

    def test_wrong_canonical_pdf_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
            build("with-base", self.one, [self.two], self.output, self.manifest)
        self.assertFalse(self.output.exists())

    def test_missing_base_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "requires --base"):
            build("with-base", None, [self.one], self.output, self.manifest)

    def test_base_forbidden_in_supplements(self):
        with self.assertRaisesRegex(ValueError, "forbids --base"):
            build("supplements", self.one, [self.two], self.output, self.manifest)

    def test_duplicate_input_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            build("supplements", None, [self.one, self.one], self.output, self.manifest)

    def test_missing_chapter_rejected(self):
        with self.assertRaises(FileNotFoundError):
            build("supplements", None, [self.root / "missing.pdf"], self.output, self.manifest)

    def test_overwrite_input_rejected(self):
        with self.assertRaisesRegex(ValueError, "overwrite"):
            build("supplements", None, [self.one], self.one, self.manifest)

    def test_output_manifest_collision_rejected(self):
        with self.assertRaisesRegex(ValueError, "distinct"):
            build("supplements", None, [self.one], self.output, self.output)

    def test_strict_byte_limit(self):
        with patch("scripts.assemble_tom1.MAX_BYTES", 100):
            with self.assertRaisesRegex(ValueError, "size limit"):
                build("supplements", None, [self.one], self.output, self.manifest)
        self.assertFalse(self.output.exists())

    def test_blank_page_rejected(self):
        from pypdf import PdfWriter
        blank = self.root / "blank.pdf"
        writer = PdfWriter()
        writer.add_blank_page(width=595, height=842)
        with blank.open("wb") as stream:
            writer.write(stream)
        with self.assertRaisesRegex(ValueError, "Blank/textless"):
            build("supplements", None, [blank], self.output, self.manifest)

    def test_hardcoded_canonical_constraints(self):
        self.assertEqual(CANONICAL_PAGES, 864)
        self.assertEqual(MAX_BYTES, 99_000_000)


if __name__ == "__main__":
    unittest.main()
