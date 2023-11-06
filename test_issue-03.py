from one_hot_encoder import fit_transform
import unittest


class TestCountLetters(unittest.TestCase):
    def test_cities(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_letters(self):
        actual = fit_transform('ab')
        expected = [
            ('ab', [1])
        ]
        self.assertEqual(actual, expected)

    def test_systems(self):
        not_expected = ('Windows', [1, 1, 0])
        actual = fit_transform(['Windows', 'MacOS', 'Linux'])
        self.assertNotIn(not_expected, actual)

    def test_empty_sequence(self):
        self.assertRaises(TypeError, fit_transform())
