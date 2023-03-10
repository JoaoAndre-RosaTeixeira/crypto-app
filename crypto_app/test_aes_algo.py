
from crypto_app.aes_algo import AdvancedEncryptionStandard


class TestAdvancedEncryptionStandard:

    def setup_method(self):
        self.aes = AdvancedEncryptionStandard()

    def test_encrypt_decrypt(self):
        message = "This is a secret message"
        key = "mysecretpassword"
        encrypted_message = self.aes.encrypt(message, key)
        decrypted_message = self.aes.decrypt(encrypted_message, key)
        assert decrypted_message == message

    def test_encrypt_with_wrong_message_type(self):
        message = 123
        key = "mysecretpassword"
        result = self.aes.encrypt(message, key)
        assert result is False

    def test_encrypt_with_wrong_key_type(self):
        message = "This is a secret message"
        key = 123
        result = self.aes.encrypt(message, key)
        assert result is False

    def test_encrypt_with_wrong_key_length(self):
        message = "This is a secret message"
        key = "shortkey"
        result = self.aes.encrypt(message, key)
        assert result is False

    def test_decrypt_with_wrong_message_type(self):
        message = 123
        key = "mysecretpassword"
        result = self.aes.decrypt(message, key)
        assert result is False

    def test_decrypt_with_wrong_key_type(self):
        message = "encrypted message"
        key = 123
        result = self.aes.decrypt(message, key)
        assert result is False

    def test_decrypt_with_wrong_key_length(self):
        message = "encrypted message"
        key = "shortkey"
        result = self.aes.decrypt(message, key)
        assert result is False

    def test_decrypt_with_wrong_key(self):
        message = "encrypted message"
        correct_key = "mysecretpassword"
        wrong_key = "wrongpassword"
        encrypted_message = self.aes.encrypt(message, correct_key)
        result = self.aes.decrypt(encrypted_message, wrong_key)
        assert result == 0