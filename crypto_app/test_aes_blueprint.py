import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, request
from crypto_app.aes_blueprint import AESBlueprint

class TestAESBlueprint:

    def setup_method(self):
        self.app = Flask(__name__)
        self.aes_blueprint = AESBlueprint()
        self.app.register_blueprint(self.aes_blueprint)

    def test_AES(self):
        with self.app.test_request_context(), \
                patch("crypto_app.aes_blueprint.render_template") as mock_render_template:
            self.aes_blueprint.AES()
            mock_render_template.assert_called_with(
                "aes.html",
                mode="homepage",
                allAlgos=self.aes_blueprint._allAlgosSorted,
                historicalAlgos=self.aes_blueprint._historicalAlgosSorted,
                outdatedAlgos=self.aes_blueprint._outdatedAlgosSorted,
                modernAlgos=self.aes_blueprint._modernAlgosSorted,
                hashingAlgos=self.aes_blueprint._hashingAlgosSorted
            )

    def test_displayEncryptedText_with_valid_input(self):
        with self.app.test_request_context(), \
                patch("crypto_app.aes_blueprint.render_template") as mock_render_template, \
                patch.object(self.aes_blueprint.algo, "encrypt", return_value="encrypted message") as mock_encrypt:
            request.form = {"message": "test message", "key_area": "16characterkey!!!"}
            self.aes_blueprint.displayEncryptedText()
            mock_encrypt.assert_called_with("test message", "16characterkey!!!")
            mock_render_template.assert_called_with(
                "aes.html",
                mode="displayEncryptedText",
                encryptedMessage="encrypted message",
                allAlgos=self.aes_blueprint._allAlgosSorted,
                historicalAlgos=self.aes_blueprint._historicalAlgosSorted,
                outdatedAlgos=self.aes_blueprint._outdatedAlgosSorted,
                modernAlgos=self.aes_blueprint._modernAlgosSorted,
                hashingAlgos=self.aes_blueprint._hashingAlgosSorted
            )

    def test_displayEncryptedText_with_invalid_key(self):
        with self.app.test_request_context(), \
                patch("crypto_app.aes_blueprint.render_template") as mock_render_template:
            request.form = {"message": "test message", "key_area": "invalid key"}
            self.aes_blueprint.displayEncryptedText()
            mock_render_template.assert_called_with(
                "aes.html",
                mode="encryptionError",
                error=("This key is not valid. Please enter a key of 128, 192 or 256 bits. "
                       "This amounts to 16, 24 or 32 characters in ASCII"),
                allAlgos=self.aes_blueprint._allAlgosSorted,
                historicalAlgos=self.aes_blueprint._historicalAlgosSorted,
                outdatedAlgos=self.aes_blueprint._outdatedAlgosSorted,
                modernAlgos=self.aes_blueprint._modernAlgosSorted,
                hashingAlgos=self.aes_blueprint._hashingAlgosSorted
            )

    def test_displayDecryptedText_with_valid_input(self):
        with self.app.test_request_context(), \
                patch("crypto_app.aes_blueprint.render_template") as mock_render_template, \
                patch.object(self.aes_blueprint.algo, "decrypt", return_value="decrypted message") as mock_decrypt:
            request.form = {"message": "68656c6c6f", "key_area": "16characterkey!!!"}
            self.aes_blueprint.displayDecryptedText()
            mock_decrypt.assert_called_with("68656c6c6f", "16characterkey!!!")
            mock_render_template.assert_called_with(
                "aes.html",
                mode="displayDecryptedText",
                decryptedMessage="decrypted message",
                allAlgos=self.aes_blueprint._allAlgosSorted,
                historicalAlgos=self.aes_blueprint._historicalAlgosSorted,
                outdatedAlgos=self.aes_blueprint._outdatedAlgosSorted,
                modernAlgos=self.aes_blueprint._modernAlgosSorted,
                hashingAlgos=self.aes_blueprint._hashingAlgosSorted
            )

    def test_displayDecryptedText_with_invalid_key(self):
        with self.app.test_request_context(), \
                patch("crypto_app.aes_blueprint.render_template") as mock_render_template, \
                patch.object(self.aes_blueprint.algo, "decrypt", return_value=0) as mock_decrypt:
            request.form = {"message": "68656c6c6f", "key_area": "invalid key"}
            self.aes_blueprint.displayDecryptedText()
            mock_decrypt.assert_called_with("68656c6c6f", "invalid key")
            mock_render_template.assert_called_with(
                "aes.html",
                mode="decryptionError",
                error=("Error during the decryption of the message. Please make sure you are using a valid key"),
                allAlgos=self.aes_blueprint._allAlgosSorted,
                historicalAlgos=self.aes_blueprint._historicalAlgosSorted,
                outdatedAlgos=self.aes_blueprint._outdatedAlgosSorted,
                modernAlgos=self.aes_blueprint._modernAlgosSorted,
                hashingAlgos=self.aes_blueprint._hashingAlgosSorted
            )

    def test_displayDecryptedText_with_invalid_message(self):
        with self.app.test_request_context(), \
                patch("crypto_app.aes_blueprint.render_template") as mock_render_template, \
                patch.object(self.aes_blueprint.algo, "decrypt", return_value=1) as mock_decrypt:
            request.form = {"message": "invalid message", "key_area": "16characterkey!!!"}
            self.aes_blueprint.displayDecryptedText()
            mock_decrypt.assert_called_with("invalid message", "16characterkey!!!")
            mock_render_template.assert_called_with(
                "aes.html",
                mode="decryptionError",
                error=("Error during the decryption of the message. Please make sure the message "
                       "you want to decrypt is encoded in hexadecimal"),
                allAlgos=self.aes_blueprint._allAlgosSorted,
                historicalAlgos=self.aes_blueprint._historicalAlgosSorted,
                outdatedAlgos=self.aes_blueprint._outdatedAlgosSorted,
                modernAlgos=self.aes_blueprint._modernAlgosSorted,
                hashingAlgos=self.aes_blueprint._hashingAlgosSorted
            )