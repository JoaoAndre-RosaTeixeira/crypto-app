import pytest
from crypto_app.blowfish_algo import Blowfish


class TestBlowfish:

    def test_valid_message(self):
        bf = Blowfish()
        message = "This is a secret message"
        key = "a_valid_key"
        assert bf.decrypt(bf.encrypt(message, key), key) == message

    def test_invalid_message(self):
        bf = Blowfish()
        message = 123
        key = "a_valid_key"
        assert bf.encrypt(message, key) == False

    def test_encrypt_decrypt(self):
        bf = Blowfish()
        message = "This is a secret message"
        key = "My secret key"
        encrypted_message = bf.encrypt(message, key)
        decrypted_message = bf.decrypt(encrypted_message, key)
        assert message == decrypted_message

    def test_invalid_message_type(self):
        bf = Blowfish()
        message = 1234
        key = "My secret key"
        assert bf.encrypt(message, key) == False
        assert bf.decrypt(message, key) == False

    def test_invalid_encrypted_message(self):
        bf = Blowfish()
        message = "This is a secret message"
        key = "My secret key"
        encrypted_message = bf.encrypt(message, key)

        # modify the encrypted message to make it invalid (change the last character)
        invalid_message = encrypted_message[:-1] + 'x'

        assert bf.decrypt(invalid_message, key) == 1

    def test_wrong_key(self):
        bf = Blowfish()
        message = "This is a secret message"
        key = "My secret key"
        encrypted_message = bf.encrypt(message, key)

        # try to decrypt with the wrong key
        wrong_key = "My wrong key"
        assert bf.decrypt(encrypted_message, wrong_key) == 0
