import unittest
from evens import evenEvens

class TestEvens(unittest.TestCase):
    def test_throws_error_if_no_value_passed_in(self):
        self.assertRaises(TypeError, evenEvens, 4)

    def test_values_in_list(self):
        self.assertEqual(evenEvens([]), False)
        self.assertEqual(evenEvens([2, 4]), True)
        self.assertEqual(evenEvens([6]), False)


if __name__ == "__main__":
    unittest.main()