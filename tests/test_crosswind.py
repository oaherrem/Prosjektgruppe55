
import unittest
import sys
import os
import pytest

# Adjust the path to the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from crosswind import is_crosswind


class TestCrosswindFunction(unittest.TestCase):

    def test_below_threshold(self):
        self.assertFalse(is_crosswind(90, 100, 20))  # under 35 m/s

    def test_direct_headwind(self):
        self.assertFalse(is_crosswind(90, 90, 40))  # rett mot rullebane

    def test_direct_tailwind(self):
        self.assertFalse(is_crosswind(90, 270, 40))  # rett bakfra

    def test_crosswind_right_angle(self):
        self.assertTrue(is_crosswind(90, 0, 40))  # vinkelrett fra nord

    def test_crosswind_near_edge(self):
        self.assertFalse(is_crosswind(90, 135, 40))  # akkurat 45° vinkel (ikke > 45)

    def test_crosswind_above_edge(self):
        self.assertTrue(is_crosswind(90, 136, 40))  # akkurat over grensa

    def test_wraparound_crosswind(self):
        self.assertTrue(is_crosswind(350, 80, 40))  # test som krysser 0°

    def test_wraparound_not_crosswind(self):
        self.assertFalse(is_crosswind(350, 10, 40))  # for nær 0°

    def test_runway_angle_on_edge(self):
        self.assertFalse(is_crosswind(135, 90, 40))  # grenseverdi for rullebane

    def test_symmetry_case(self):
        self.assertTrue(is_crosswind(180, 90, 50))  # ren sidevind fra øst


if __name__ == "__main__":
    unittest.main()
