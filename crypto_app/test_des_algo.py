import pytest
from crypto_app.des_algo import DES

class TestDES:

    def setup_method(self):
        self.des = DES()

    def test_encrypt_decrypt(self):
        message = "hello world"
        key = "secret12"
        encrypted = self.des.encrypt(message, key)
        decrypted = self.des.decrypt(encrypted, key)
        assert decrypted == message

    def test_invalid_message(self):
        message = 1234
        key = "secret12"
        result = self.des.encrypt(message, key)
        assert result == False

    def test_invalid_key(self):
        message = "hello world"
        key = "secret" # wrong length
        result = self.des.encrypt(message, key)
        assert result == False

        key = "not ascii" # not ascii
        result = self.des.encrypt(message, key)
        assert result == False

    def test_wrong_key(self):
        message = "hello world"
        key1 = "secret12"
        key2 = "notthesame"
        encrypted = self.des.encrypt(message, key1)
        decrypted = self.des.decrypt(encrypted, key2)
        assert decrypted == 0 # wrong key

    def test_hex_encoding(self):
        message = "hello world"
        key = "secret12"
        encrypted = self.des.encrypt(message, key)
        assert isinstance(encrypted, str) and len(encrypted) % 2 == 0
        decrypted = self.des.decrypt(encrypted, key)
        assert decrypted == message
