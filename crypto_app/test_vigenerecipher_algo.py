import pytest
from crypto_app.vigenerecipher_algo import VigenereCipher

class TestVigenereCipher:

    def setup_method(self):
        self.vigenere = VigenereCipher()

    def test_encrypt_decrypt(self):
        message = "hello world"
        key = "secret"
        encrypted = self.vigenere.encrypt(message, key)
        decrypted = self.vigenere.decrypt(encrypted, key)
        assert decrypted == message

    def test_empty_key(self):
        message = "hello world"
        key = ""
        result = self.vigenere.encrypt(message, key)
        assert result == False

    def test_special_characters_key(self):
        message = "hello world"
        key = "sécret"
        result = self.vigenere.encrypt(message, key)
        assert result == False

    def test_invalid_input(self):
        message = 1234
        key = "secret"
        result = self.vigenere.encrypt(message, key)
        assert result == False
