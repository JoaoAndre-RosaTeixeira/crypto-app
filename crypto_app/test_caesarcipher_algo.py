import pytest
from crypto_app.caesarcipher_algo import CaesarCipher

class TestCaesarCipher:

    def test_encrypt_string(self):
        cc = CaesarCipher()
        result = cc.encrypt("hello world", 3)
        assert result == "khoor zruog"

    def test_decrypt_string(self):
        cc = CaesarCipher()
        result = cc.decrypt("khoor zruog", 3)
        assert result == "hello world"

    def test_encrypt_integer_message(self):
        cc = CaesarCipher()
        result = cc.encrypt(1234, 3)
        assert result == False

    def test_encrypt_non_integer_key(self):
        cc = CaesarCipher()
        result = cc.encrypt("hello world", "3")
        assert result == False

    def test_decrypt_non_string_message(self):
        cc = CaesarCipher()
        result = cc.decrypt(1234, 3)
        assert result == False

    def test_decrypt_non_integer_key(self):
        cc = CaesarCipher()
        result = cc.decrypt("khoor zruog", "3")
        assert result == False

