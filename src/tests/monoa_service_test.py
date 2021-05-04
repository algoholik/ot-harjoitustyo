import unittest
from datetime import datetime
from entities.note import Note
from entities.snip import Snip
from services.monoa_service import MonoaService

class TestMonoaService(unittest.TestCase):
    def setUp(self):
        self.monoa_service = MonoaService()
        self.timetest = datetime.now()
        self.testsnip = Snip(1, 0, "Snip content", self.timetest)
        self.testnote = Note(1, "Note title", [self.testsnip], self.timetest)

    def test_get_note_by_id_returns_object_correctly(self):
        self.assertEqual(self.monoa_service.get_note_by_id(1).get_id(), 1)

    def test_get_snip_by_id_returns_object_correctly(self):
        self.assertEqual(self.monoa_service.get_snip_by_id(1).get_id(), 1)

    def test_get_latest_note_id_returns_id_as_int_correctly(self):
        self.assertEqual(self.monoa_service.get_latest_note_id(), 1)
