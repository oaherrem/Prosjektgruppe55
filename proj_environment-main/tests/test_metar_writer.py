import unittest
import sys
import os

# Adjust the path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from metar_writer import get_metar

class TestMetarWriter(unittest.TestCase):
    def test_get_metar(self):
        metar = get_metar("ENOL", "2025-01-01") # Henter en vilkårlig flyplass og dato
        self.assertTrue(metar.startswith("ENOL")) # Tester om dataen blir hentet fra riktig flyplass
        self.assertEqual(metar.count('='), 48) # Sjekker at dataen har 48 linjer, da = tegn betyr at det spesifikke datalinjen er ferdig

if __name__ == '__main__':
    unittest.main()
