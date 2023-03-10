import unittest
from crypto_app.vigenerecipher_algo import VigenereCipher

class TestVigenereCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = VigenereCipher()

    def test_encrypt_valid_input(self):
        message = "hello world"
        key = "secret"
        expected_output = "zincs ostch"
        self.assertEqual(self.cipher.encrypt(message, key), expected_output)

    def test_encrypt_invalid_input(self):
        message = 123
        key = "secret"
        self.assertFalse(self.cipher.encrypt(message, key))

    def test_decrypt_valid_input(self):
        message = "zincs ostch"
        key = "secret"
        expected_output = "hello world"
        self.assertEqual(self.cipher.decrypt(message, key), expected_output)

    def test_decrypt_invalid_input(self):
        message = "wzmqc oyasd"
        key = 123
        self.assertFalse(self.cipher.decrypt(message, key))

if __name__ == '__main__':
    unittest.main()
