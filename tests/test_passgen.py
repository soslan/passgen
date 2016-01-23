import unittest
from passgen import passgen


class TestPassgen(unittest.TestCase):

    def test_errors(self):
        with self.assertRaises(ValueError):
            passgen(length=-2)

        with self.assertRaises(ValueError):
            passgen(case="spam")

        with self.assertRaises(ValueError):
            passgen(digits=False, letters=False)

    def test_case(self):
        password = passgen(case='upper')
        self.assertEqual(password, password.upper())

        password = passgen(case='lower')
        self.assertEqual(password, password.lower())

    def test_length(self):
        password = passgen(length=10)
        self.assertEqual(len(password), 10)

        password = passgen(length=15, case='upper', digits=False)
        self.assertEqual(len(password), 15)

if __name__ == '__main__':
    unittest.main()
