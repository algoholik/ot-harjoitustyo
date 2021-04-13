import unittest
from entities.note import Note
from entities.snippet import Snippet
from datetime import datetime

class TestSnippet(unittest.TestCase):
    def setUp(self):
        self.timetest = datetime.now()
        self.testsnippet = Snippet(123, "This is a snippet", self.timetest)
        
    def test_snippet_object_is_being_created(self):
        self.assertTrue(self.testsnippet)

    def test_snippet_prints_to_str_correctly(self):
        self.assertEqual(str(self.testsnippet), f"snippet id: 123 (created {self.timetest}): This is a snippet")

    def test_snippet_returns_id_correctly(self):
        self.assertEqual(self.testsnippet.get_id(), 123)

    def test_snippet_returns_content_correctly(self):
        self.assertEqual(self.testsnippet.get_snippet(), "This is a snippet")

    def test_snippet_returns_updated_timestamp_correctly(self):
        self.assertEqual(self.testsnippet.get_updated(), self.timetest)
