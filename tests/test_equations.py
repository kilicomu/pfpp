"""#############################################################################
test_equations.py
================================================================================
Unit tests for the equations module of pfpp.
#############################################################################"""
import unittest
# ------------------------------------------------------------------------------
from pfpp import equations as eqn
# ------------------------------------------------------------------------------
class TestEquations(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_computation_time(self):
        self.assertEqual(eqn.computation_time(1, 1, 1, 1), 3)
