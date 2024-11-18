import unittest
import regular_expression


class TestRegex(unittest.TestCase):
    def test_file(self):
        self.assertTrue(regular_expression.find_in_file('Article_about_UTC.txt'))
        self.assertFalse(regular_expression.find_in_file('UTC.txt'))

    def test_right_choice(self):
        self.assertEqual(regular_expression.checking_the_input('UTC+12:30, UTC-32'), ['UTC+12:30'])

    def test_no_correct_values(self):
        self.assertEqual(regular_expression.checking_the_input('UTC+32'), None)

if __name__ == '__main__':
    unittest.main()