import unittest
from entities.note import Note
from entities.snip import Snip
from datetime import datetime

class TestNote(unittest.TestCase):
    def setUp(self):
        self.timetest = datetime.now()
        self.testnote = Note(33, "Note name", "Note content", self.timetest)

    def test_note_object_is_being_created(self):
        self.assertTrue(self.testnote)

    def test_snip_returns_id_correctly(self):
        self.assertEqual(self.testnote.get_id(), 33)

    def test_note_returns_name_correctly(self):
        self.assertEqual(self.testnote.get_name(), "Note name")

    def test_note_returns_content_correctly(self):
        self.assertEqual(self.testnote.get_content(), "Note content")

    def test_note_returns_timestamp_correctly(self):
        self.assertEqual(self.testnote.get_timestamp(), self.timetest)

    def test_note_prints_to_str_correctly(self):
        self.assertEqual(str(self.testnote), f"33\nNote name\nNote content\n{self.timetest}")

    def test_note_repr_prints_correctly(self):
        self.assertEqual(repr(self.testnote), f"33\nNote name\nNote content\n{self.timetest}")

    def test_note_sets_id_correctly(self):
        self.testnote.set_id(34)
        self.assertEqual(self.testnote.get_id(), 34)

    def test_note_sets_name_correctly(self):
        self.testnote.set_name("Note name modified")
        self.assertEqual(self.testnote.get_name(), "Note name modified")

    def test_note_sets_content_correctly(self):
        self.testnote.set_content("Note content modified")
        self.assertEqual(self.testnote.get_content(), "Note content modified")

    def test_note_sets_timestamp_correctly(self):
        self.timetest2 = datetime.now()
        self.testnote.set_timestamp(self.timetest2)
        self.assertEqual(self.testnote.get_timestamp(), self.timetest2)
