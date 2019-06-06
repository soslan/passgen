import unittest
import re
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

    def test_limit_punctuation(self):
        pl = '.'
        password = passgen(letters=True, digits=False, length=6,
                           punctuation=True, limit_punctuation=pl)
        password = re.sub(r"[a-zA-Z.]", "", password)
        self.assertTrue(password == '')

    def test_only_letters(self):
        password = passgen(letters=True, digits=False)
        password = re.sub(r"[a-zA-Z]", "", password)
        self.assertTrue(password == '')

    def test_only_digits(self):
        password = passgen(letters=False, digits=True)
        password = re.sub(r"[0-9]", "", password)
        self.assertTrue(password == '')

    def test_class_always_occurs(self):
        # Generating 4-char password with all classes
        for i in range(1, 100):
            password = passgen(punctuation=True, case='both', length=4)
            password = re.sub(r"[0-9]", "", password)
            self.assertTrue(len(password) == 3)
            password = re.sub(r"[a-z]", "", password)
            self.assertTrue(len(password) == 2)
            password = re.sub(r"[A-Z]", "", password)
            self.assertTrue(len(password) == 1)


if __name__ == '__main__':
    unittest.main()
