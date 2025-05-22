import unittest
import sys
import os
import pytest
import requests
from unittest.mock import patch, Mock

#Justerer filbanen til 'src'-mappa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from metar_writer import get_metar

class TestMetarWriter(unittest.TestCase):
    def test_valid_get_metar(self):
        metar = get_metar("ENOL", "2025-01-01") # Henter en vilkårlig flyplass og dato
        self.assertTrue(metar.startswith("ENOL")) # Tester om dataen blir hentet fra riktig flyplass
        self.assertEqual(metar.count('='), 48) # Sjekker at dataen har 48 linjer, da = tegn betyr at det spesifikke datalinjen er ferdig

    
    def test_invalid_date_format_causes_exit(self):
        with patch.dict(os.environ, {"base_url": "http://example.com"}), \
            patch("os.getcwd", return_value="/home/UnknownUser"):
            
            with pytest.raises(SystemExit) as e:
                get_metar("ENVA", "2020-12-31")
            assert e.value.code == 1

    def test_invalid_icao_code(self):
        with patch.dict(os.environ, {"base_url": "http://example.com"}), \
             patch("os.getcwd", return_value="/home/Ole"), \
             patch("requests.get") as mock_get:

            mock_get.return_value.text = "Invalid ICAO"

            result = get_metar("12", "20250101")
            assert "Invalid" in result

    def test_invalid_user_causes_exit(self):
        with patch.dict(os.environ, {"base_url": "http://example.com"}), \
             patch("os.getcwd", return_value="/users/unknown"):

            with pytest.raises(SystemExit) as e:
                get_metar("ENVA", "20250101")
            assert e.value.code == 1

    def test_requests_failure(self):
        with patch.dict(os.environ, {"base_url": "http://example.com"}), \
             patch("os.getcwd", return_value="/home/hanna"), \
             patch("requests.get", side_effect=requests.exceptions.RequestException("Network error")):

            with pytest.raises(requests.exceptions.RequestException):
                get_metar("ENVA", "20250101")


if __name__ == '__main__':
    unittest.main()
