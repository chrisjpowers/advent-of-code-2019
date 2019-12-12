import unittest
from advent import Password, Password2


class TestPassword(unittest.TestCase):
    def test_validity(self):
        self.assertEqual(Password(111111).valid, True)
        self.assertEqual(Password(123356).valid, True)
        self.assertEqual(Password(123456).valid, False)
        self.assertEqual(Password(223450).valid, False)

class TestPassword2(unittest.TestCase):
    def test_validity(self):
        self.assertEqual(Password2(111111).valid, False)
        self.assertEqual(Password2(111122).valid, True)
        self.assertEqual(Password2(112222).valid, True)
        self.assertEqual(Password2(123356).valid, True)
        self.assertEqual(Password2(123456).valid, False)
        self.assertEqual(Password2(223450).valid, False)