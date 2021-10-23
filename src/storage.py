import json
from random import shuffle
from typing import Dict, List
from aes_cipher import DataEncrypter, DataDecrypter


class Storage:
    codes_by_service: Dict[str, List[str]] = {}

    def __init__(self, codes_by_service: Dict[str, List[str]]) -> None:
        self.codes_by_service = codes_by_service

    @staticmethod
    def from_json(json_str: str) -> 'Storage':
        """
        Creates a Storage object from a json string.
        """
        return json.loads(json_str)

    @staticmethod
    def decrypt(encrypted: str, passwords: List[str], salt=None) -> 'Storage':
        """
        Decrypts a json string to a Storage object.
        """
        decipher = DataDecrypter()
        decipher.Decrypt(encrypted, passwords, salt=salt)
        return Storage.from_json(
            decipher.GetDecryptedData()
        )

    def to_json(self) -> str:
        """
        Returns a json string representation of the Storage object.
        """
        return json.dumps(self.codes_by_service)

    def get_codes_by_service(self, service: str):
        """
        Gets the codes for a service.
        """
        return self.codes_by_service.get(service, [])

    def get_random_codes(self, service: str, n: int):
        """
        Gets n random codes for a service.
        """
        codes = self.get_codes_by_service(service).copy()
        shuffle(codes)

        if len(codes) < n:
            return codes
        return codes[:n]

    def encrypt(self, passwords: List[str], salt: str = None) -> bytes:
        """
        Encrypts the Storage object to bytes.
        """
        cipher = DataEncrypter()
        cipher.Encrypt(self.to_json(), passwords, salt=salt)
        return cipher.GetEncryptedData()
