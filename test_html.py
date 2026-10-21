
from pathlib import Path
import unittest
from html.parser import HTMLParser

HTML_FILE = Path(__file__).parent / "index.html"


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class TestRegistrationForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML_FILE.read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(cls.html)

    def test_html_file_exists(self):
        self.assertTrue(HTML_FILE.exists())

    def test_form_exists(self):
        self.assertTrue(any(
            tag == "form" for tag, attrs in self.parser.elements
        ))

    def test_name_field(self):
        self.assertTrue(any(
            attrs.get("name") == "name"
            for tag, attrs in self.parser.elements if tag == "input"
        ))

    def test_email_field(self):
        self.assertTrue(any(
            attrs.get("type") == "email"
            for tag, attrs in self.parser.elements if tag == "input"
        ))

    def test_contact_field(self):
        self.assertTrue(any(
            attrs.get("name") == "contact"
            for tag, attrs in self.parser.elements if tag == "input"
        ))

    def test_submit_button(self):
        self.assertTrue(any(
            tag == "button" and attrs.get("type") == "submit"
            for tag, attrs in self.parser.elements
        ))


if __name__ == "__main__":
    unittest.main()
