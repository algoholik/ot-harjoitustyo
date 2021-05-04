import unittest
from entities.note import Note
from entities.snip import Snip
from datetime import datetime

class TestNote(unittest.TestCase):
    def setUp(self):
        self.timetest = datetime.now()
        self.testnote = Note(33, "Note title", [Snip(123, 0, "Snip content", self.timetest)], self.timetest)

    def test_note_object_is_being_created(self):
        self.assertTrue(self.testnote)

    def test_snip_returns_id_correctly(self):
        self.assertEqual(self.testnote.get_id(), 33)

    def test_note_returns_title_correctly(self):
        self.assertEqual(self.testnote.get_title(), "Note title")

    def test_note_returns_contents_correctly(self):
        self.assertEqual(self.testnote.get_contents(), "Note content")

    def test_note_returns_modified_correctly(self):
        self.assertEqual(self.testnote.get_modified(), self.timetest)

    def test_note_prints_to_str_correctly(self):
        self.assertEqual(
            str(self.testnote), 
            f"Note #33 Title: Note title ({self.timetest})\nSnip #123 (0) ({self.timetest})\nSnip content\n"
        )

    def test_note_repr_prints_correctly(self):
        self.assertEqual(
            str(self.testnote), 
            f"Note #33 Title: Note title ({self.timetest})\nSnip #123 (0) ({self.timetest})\nSnip content\n"
        )

    def test_note_sets_id_correctly(self):
        self.testnote.set_id(34)
        self.assertEqual(self.testnote.get_id(), 34)

    def test_note_sets_title_correctly(self):
        self.testnote.set_title("Note title modified")
        self.assertEqual(self.testnote.get_title(), "Note title modified")

    def test_note_sets_contents_correctly(self):
        self.testnote.set_contents(Snip(234, 0, "Another snip content", self.timetest))
        comparison = f"Snip #234 (0) ({self.timetest})\nAnother snip content\n"
        self.assertEqual(self.testnote.get_contents(), comparison)

    def test_note_adds_content_correctly(self):
        self.testnote.add_content(Snip(234, 0, "Another snip content", self.timetest))
        self.assertEqual(
            self.testnote.get_contents(), 
                f"Snip #234 (0) ({self.timetest})\nAnother snip content\n" + 
                f"'Snip #234 (0) ({self.timetest})\nAnother snip content\n"
        )

    def test_note_sets_modified_correctly(self):
        self.timetest2 = datetime.now()
        self.testnote.set_modified(self.timetest2)
        self.assertEqual(self.testnote.get_modified(), self.timetest2)
