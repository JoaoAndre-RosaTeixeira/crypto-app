import unittest
from crypto_app.md5_algo import MD5

class TestMD5(unittest.TestCase):

    def setUp(self):
        self.md5 = MD5()

    def test_encrypt(self):
        message = "This is a test message"
        expected_hash = "fafb00f5732ab283681e124bf8747ed1"
        result = self.md5.encrypt(message)
        self.assertEqual(result, expected_hash)

    def test_encrypt_empty_message(self):
        message = ""
        expected_hash = "d41d8cd98f00b204e9800998ecf8427e"
        result = self.md5.encrypt(message)
        self.assertEqual(result, expected_hash)

    def test_encrypt_non_string_message(self):
        message = 12345
        expected_result = False
        result = self.md5.encrypt(message)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
