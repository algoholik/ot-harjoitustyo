import unittest
from entities.note import Note
from entities.snippet import Snippet

class TestSnippet(unittest.TestCase):
    def setUp(self):
        self.testsnippet = Snippet()

    def test_snippet_is_initialized_correctly(self):
        self.assertTrue(self.testsnippet)

