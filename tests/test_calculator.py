import subprocess
import sys
import unittest
from macros_calc import calculate_macros_and_calories as calculate


class CalculatorTests(unittest.TestCase):
    def test_male_worked_example(self):
        result = calculate(80, 180, 30, 'male', 'sedentary')
        self.assertAlmostEqual(result['bmr_kcal_per_day'], 1853.632)
        self.assertAlmostEqual(result['estimated_tdee_kcal_per_day'], 2224.3584)

    def test_female_worked_example(self):
        self.assertAlmostEqual(calculate(60, 165, 30, 'female', 'sedentary')['bmr_kcal_per_day'], 1383.683)

    def test_energy_reconciliation(self):
        result = calculate(80, 180, 30, 'male', 'moderately active')
        allocated = result['protein_g_per_day'] * 4 + result['fat_g_per_day'] * 9 + result['carbs_g_per_day'] * 4
        self.assertAlmostEqual(allocated, result['estimated_tdee_kcal_per_day'])

    def test_height_changes_estimate(self):
        short = calculate(80, 170, 30, 'male', 'sedentary')
        tall = calculate(80, 180, 30, 'male', 'sedentary')
        self.assertAlmostEqual(tall['bmr_kcal_per_day'] - short['bmr_kcal_per_day'], 47.99)

    def test_invalid_numeric_inputs(self):
        for values in ((0, 180, 30), (80, -1, 30), (80, 180, 17), (float('nan'), 180, 30), (80, float('inf'), 30), (True, 180, 30)):
            with self.subTest(values=values), self.assertRaises(ValueError):
                calculate(*values, 'male', 'sedentary')

    def test_invalid_choices_and_allocation(self):
        for sex, activity, protein, fat in [('other', 'sedentary', 2.2, .25), ('male', 'unknown', 2.2, .25), ('male', 'sedentary', 100, .25), ('male', 'sedentary', 2.2, 1), ('male', 'sedentary', -1, .25)]:
            with self.assertRaises(ValueError):
                calculate(80, 180, 30, sex, activity, protein, fat)

    def test_import_has_no_prompt(self):
        result = subprocess.run([sys.executable, '-c', 'import macros_calc'], input='', capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
