"""#############################################################################
test_equations.py
================================================================================
Unit tests for the equations module of pfpp.
#############################################################################"""
import unittest
# ------------------------------------------------------------------------------
from pfpp import equations as eqn
# ------------------------------------------------------------------------------
class TestComputationTime(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_setup_time(self):
        self.assertEqual(eqn.computation_time(1, 1, 1, 1), 3)
        self.assertEqual(eqn.computation_time(2, 1, 1, 1), 4)

    def test_compute_time(self):
        pass

    def test_finalization_time(self):
        pass

    def test_n_processing_elements(self):
        pass

    def test_setup_time_type_validity(self):
        pass

    def test_setup_time_value_validity(self):
        pass

    def test_compute_time_type_validity(self):
        pass

    def test_compute_time_value_validity(self):
        pass

    def test_finalization_time_type_validity(self):
        pass

    def test_finalization_time_value_validity(self):
        pass

    def test_n_processing_elements_type_validity(self):
        pass

    def test_n_processing_elements_value_validity(self):
        pass
