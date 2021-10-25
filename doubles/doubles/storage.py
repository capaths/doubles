import json
from random import shuffle
from typing import Dict, List
from aes_cipher import DataEncrypter, DataDecrypter

__all__ = ['Storage']

"""
Storage

This class is used to store and retrieve codes securely from different services.

Data is encrypted using AES-256.
"""
class Storage:
    codes_by_service: Dict[str, List[str]] = {}

    def __init__(self, codes_by_service: Dict[str, List[str]]):
        """
        Initializes the Storage object.
        :param codes_by_service: A dictionary of service names to a list of codes.
        """
        self.codes_by_service = codes_by_service

    @staticmethod
    def from_json(json_str: str) -> 'Storage':
        """
        Creates a Storage object from a json string.
        :param json_str: A json string.
        :return: A Storage object.
        """
        return Storage(codes_by_service=json.loads(json_str))

    def to_json(self) -> str:
        """
        Returns a json string representation of the Storage object.
        """
        return json.dumps(self.codes_by_service)

    @staticmethod
    def decrypt(encrypted: str, passwords: List[str], salt=None) -> 'Storage':
        """
        Decrypts a json string to a Storage object.
        :param encrypted: An encrypted json string.
        :param passwords: A list of passwords to use for decryption.
        :param salt: The salt to use for decryption.
        :return: A Storage object.
        """
        decipher = DataDecrypter()
        decipher.Decrypt(encrypted, passwords, salt=salt)
        return Storage.from_json(
            decipher.GetDecryptedData()
        )

    def encrypt(self, passwords: List[str], salt: str = None) -> bytes:
        """
        Encrypts the Storage object to bytes.
        :param passwords: A list of passwords to use for encryption.
        :param salt: The salt to use for encryption.
        """
        cipher = DataEncrypter()
        cipher.Encrypt(self.to_json(), passwords, salt=salt)
        return cipher.GetEncryptedData()

    def get_codes_by_service(self, service: str):
        """
        Gets the codes for a service.
        :param service: The service name.
        """
        return self.codes_by_service.get(service, [])

    def get_random_codes(self, service: str, n: int):
        """
        Gets n random codes for a service.
        :param service: The service name.
        :param n: The number of codes to get.
        """
        codes = self.get_codes_by_service(service).copy()
        shuffle(codes)

        if len(codes) < n:
            return codes
        return codes[:n]

    @property
    def services(self) -> List[str]:
        return list(self.codes_by_service.keys())
