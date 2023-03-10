import unittest
from crypto_app.sha_algo import SHA

class TestSHA(unittest.TestCase):

    def setUp(self):
        self.sha = SHA()

    def test_encrypt_valid_input(self):
        message = "hello world"
        expected_output = "309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f"
        self.assertEqual(self.sha.encrypt(message), expected_output)

    def test_encrypt_invalid_input(self):
        message = 123
        self.assertFalse(self.sha.encrypt(message))

    def test_encrypt_empty_input(self):
        message = ""
        expected_output = "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
        self.assertEqual(self.sha.encrypt(message), expected_output)

if __name__ == '__main__':
    unittest.main()
