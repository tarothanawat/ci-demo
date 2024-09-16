from unittest import TestCase
from statistics import variance, stddev, average
from math import sqrt


class StatisticsTest(TestCase):

    def test_average_typical_values(self):
        """Test the average of typical values."""
        self.assertEqual(3.0, average([1, 2, 3, 4, 5]))
        self.assertEqual(5.0, average([5, 5, 5, 5, 5]))
        self.assertEqual(6.0, average([2, 4, 6, 8, 10]))

    def test_average_with_zeros(self):
        """Test the average when the list contains zeros."""
        self.assertEqual(0.0, average([0, 0, 0, 0, 0]))
        self.assertEqual(2.0, average([0, 2, 4]))
        self.assertEqual(-2.0, average([-4, -2, 0]))

    def test_average_with_negatives(self):
        """Test the average of negative numbers."""
        self.assertEqual(-3.0, average([-1, -2, -3, -4, -5]))
        self.assertEqual(0.0, average([-1, 0, 1]))

    def test_average_empty_list(self):
        """Test that average raises a ValueError for an empty list."""
        with self.assertRaises(ValueError):
            average([])

    def test_variance_typical_values(self):
        """Test variance with typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """Test variance with decimal values."""
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_variance_single_value(self):
        """Test variance with a single value."""
        self.assertEqual(0.0, variance([10]))

    def test_variance_with_zeros(self):
        """Test variance when the list contains zeros."""
        self.assertAlmostEqual(0.0, variance([0, 0, 0, 0, 0]))
        self.assertAlmostEqual(2.6667, variance([0, 2, 4]), places=4)

    def test_variance_with_negatives(self):
        """Test variance of negative numbers."""
        self.assertEqual(2.0, variance([-1, -2, -3, -4, -5]))

    def test_variance_empty_list(self):
        """Test that variance raises a ValueError for an empty list."""
        with self.assertRaises(ValueError):
            variance([])

    def test_stddev(self):
        """Test standard deviation."""
        self.assertEqual(0.0, stddev([10.0]))
        self.assertEqual(2.0, stddev([1, 5]))
        self.assertEqual(sqrt(0.5), stddev([0, 0.5, 1, 1.5, 2]))
        self.assertEqual(0.0, stddev([0, 0, 0]))
        self.assertAlmostEqual(0.8165, stddev([1, 2, 3]), places=4)

    def test_average_large_numbers(self):
        """Test average with large numbers."""
        self.assertEqual(1000000000.0, average([1000000000, 1000000000, 1000000000]))

    def test_variance_large_numbers(self):
        """Test variance with large numbers."""
        self.assertAlmostEqual(250000000000000000.0, variance([0, 1000000000]))

    def test_stddev_large_numbers(self):
        """Test standard deviation with large numbers."""
        self.assertEqual(500000000.0, stddev([0, 1000000000]))


