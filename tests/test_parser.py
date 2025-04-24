# tests/test_parser.py
import unittest
from src.parser import parse_html, parse_pdf, parse_doc, parse_docx, parse_djvu

class TestParser(unittest.TestCase):

    def test_parse_html(self):
        self.assertIsNone(parse_html('test.html'))

    def test_parse_pdf(self):
        self.assertIsNone(parse_pdf('test.pdf'))

    def test_parse_doc(self):
        self.assertIsNone(parse_doc('test.doc'))

    def test_parse_docx(self):
        self.assertIsNone(parse_docx('test.docx'))

    def test_parse_djvu(self):
        self.assertIsNone(parse_djvu('test.djvu'))

if __name__ == '__main__':
    unittest.main()