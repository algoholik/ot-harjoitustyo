import unittest
import os

from utils import get_file_path

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.filename = "filename.txt"
        self.cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    def test_get_file_path_returns_correct_path(self):
        self.assertEqual(get_file_path("tests/filename.txt"), os.path.join(self.cwd, self.filename))
