import unittest
import sys
import os

# Adjust the path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from taf_writer import get_taf

class TestTafWriter(unittest.TestCase):
    def test_get_taf(self):
        taf = get_taf("ENVA", "2025-01-01") # Henter en vilkårlig flyplass og dato
        self.assertTrue(taf.startswith("ENVA")) # Tester om dataen blir hentet fra riktig flyplass

if __name__ == '__main__':
    unittest.main()
