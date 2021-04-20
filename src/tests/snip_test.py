import unittest
from entities.note import Note
from entities.snip import Snip
from datetime import datetime

class TestSnip(unittest.TestCase):
    def setUp(self):
        self.timetest = datetime.now()
        self.testsnip = Snip(123, "Snip name", "Snip content", self.timetest)

    def test_snip_object_is_being_created(self):
        self.assertTrue(self.testsnip)

    def test_snip_returns_id_correctly(self):
        self.assertEqual(self.testsnip.get_id(), 123)

    def test_snip_returns_name_correctly(self):
        self.assertEqual(self.testsnip.get_name(), "Snip name")

    def test_snip_returns_content_correctly(self):
        self.assertEqual(self.testsnip.get_content(), "Snip content")

    def test_snip_returns_timestamp_correctly(self):
        self.assertEqual(self.testsnip.get_timestamp(), self.timetest)

    def test_snip_prints_to_str_correctly(self):
        self.assertEqual(str(self.testsnip), f"123\nSnip name\nSnip content\n{self.timetest}")

    def test_snip_repr_prints_correctly(self):
        self.assertEqual(repr(self.testsnip), f"123\nSnip name\nSnip content\n{self.timetest}")

    def test_snip_sets_id_correctly(self):
        self.testsnip.set_id(124)
        self.assertEqual(self.testsnip.get_id(), 124)

    def test_snip_sets_name_correctly(self):
        self.testsnip.set_name("Snip name modified")
        self.assertEqual(self.testsnip.get_name(), "Snip name modified")

    def test_snip_sets_content_correctly(self):
        self.testsnip.set_content("Snip content modified")
        self.assertEqual(self.testsnip.get_content(), "Snip content modified")

    def test_snip_sets_timestamp_correctly(self):
        self.timetest2 = datetime.now()
        self.testsnip.set_timestamp(self.timetest2)
        self.assertEqual(self.testsnip.get_timestamp(), self.timetest2)
