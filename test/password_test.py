import unittest
from advent import Password


class TestPassword(unittest.TestCase):
    def test_validity(self):
        self.assertEqual(Password(111111).valid, True)
        self.assertEqual(Password(123356).valid, True)
        self.assertEqual(Password(123456).valid, False)
        self.assertEqual(Password(223450).valid, False)

