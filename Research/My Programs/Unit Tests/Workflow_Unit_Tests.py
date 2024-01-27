import unittest

import numpy as np
import pandas as pd

from Align_Data import find_deviation_point, find_percentile_index
from Calculate_Linear_Fit_Sensor_Calibrations import calculate_linear_fit


class TestFindDeviationPoint(unittest.TestCase):
    def test_deviation_point(self):
        data = pd.DataFrame({'value': [1, 1, 1, 1, 5, 6, 7, 8, 9, 10, 11]})
        column = 'value'
        baseline = 2
        deviation_threshold = 3
        expected_result = 4  # Index where deviation starts
        result = find_deviation_point(data, column, baseline, deviation_threshold)
        self.assertEqual(result, expected_result)


class TestFindPercentileIndex(unittest.TestCase):
    def test_percentile_index(self):
        data = [1, 3, 5, 7, 9]
        percentile = 50
        expected_index = 2
        expected_value = 5
        index, value = find_percentile_index(data, percentile)
        self.assertEqual(index, expected_index)
        self.assertEqual(value, expected_value)


class TestCalculateLinearFit(unittest.TestCase):
    def test_linear_fit(self):
        excel_force = np.array([2, 4, 6, 8])
        arduino_raw_force = np.array([1, 2, 3, 4])
        expected_m, expected_c = 2, 0  # y = 2x
        m, c = calculate_linear_fit(excel_force, arduino_raw_force)
        self.assertAlmostEqual(m, expected_m)
        self.assertAlmostEqual(c, expected_c)


if __name__ == '__main__':
    unittest.main()
