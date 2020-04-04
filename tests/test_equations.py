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
    """
    Unit tests for equation 2.1 - computation time.
    """

    def setUp(self):
        """
        Test case set up.
        """
        self.failing_literals = ["1", 1 + 1j, (1,), [1]]

    def tearDown(self):
        """
        Test case tear down.
        """
        del self.failing_literals

    def test_base_case(self):
        """
        Test basic correctness of computed result.
        """
        self.assertEqual(eqn.computation_time(1, 1, 1, 1), 3)

    def test_setup_time(self):
        """
        Test correctness of varying setup_time parameter.
        """
        self.assertEqual(eqn.computation_time(2, 1, 1, 1), 4)

    def test_compute_time(self):
        """
        Test correctness of varying compute_time parameter.
        """
        self.assertEqual(eqn.computation_time(1, 2, 1, 1), 4)

    def test_finalization_time(self):
        """
        Test correctness of varying finalization_time parameter.
        """
        self.assertEqual(eqn.computation_time(1, 1, 2, 1), 4)

    def test_n_processing_elements(self):
        """
        Test correctness of varying n_processing_elements parameter.
        """
        self.assertEqual(eqn.computation_time(1, 1, 1, 2), 2.5)

    def test_setup_time_type_validity(self):
        """
        Test setup_time type checking.
        """
        for literal in self.failing_literals:
            with self.assertRaises(TypeError):
                eqn.computation_time(literal, 1, 1, 1)

    def test_setup_time_value_validity(self):
        """
        Test setup_time value checking.
        """
        with self.assertRaises(ValueError):
            eqn.computation_time(-1, 1, 1, 1)

    def test_compute_time_type_validity(self):
        """
        Test compute_time type checking.
        """
        for literal in self.failing_literals:
            with self.assertRaises(TypeError):
                eqn.computation_time(1, literal, 1, 1)

    def test_compute_time_value_validity(self):
        """
        Test compute_time value checking.
        """
        with self.assertRaises(ValueError):
            eqn.computation_time(1, -1, 1, 1)

    def test_finalization_time_type_validity(self):
        """
        Test finalization_time type checking.
        """
        for literal in self.failing_literals:
            with self.assertRaises(TypeError):
                eqn.computation_time(1, 1, literal, 1)

    def test_finalization_time_value_validity(self):
        """
        Test finalization time value checking.
        """
        with self.assertRaises(ValueError):
            eqn.computation_time(1, 1, -1, 1)

    def test_n_processing_elements_type_validity(self):
        """
        Test n_processing_elements type checking.
        """
        for literal in self.failing_literals:
            with self.assertRaises(TypeError):
                eqn.computation_time(1, 1, 1, literal)
        # Special case for n_processing_elements, as it should throw an error
        # with a float:
        with self.assertRaises(TypeError):
            eqn.computation_time(1, 1, 1, 1.5)

    def test_n_processing_elements_value_validity(self):
        """
        Test n_processing_elements value checking.
        """
        with self.assertRaises(ValueError):
            eqn.computation_time(1, 1, 1, 0)

        with self.assertRaises(ValueError):
            eqn.computation_time(1, 1, 1, -1)
