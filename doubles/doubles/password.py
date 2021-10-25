import base58
import secrets
from string import ascii_uppercase, digits


JOINER = ':'

__all__ = ['StoragePassword']

class StoragePassword:
    """
    Class that stores a password for the storage.
    """

    index: int
    secret: str


    def __init__(self, index: int, secret: str):
        """
        Constructor.
        :param index: The index part of the password.
        :param secret: The secret part of the password.
        """
        self.index = index
        self.secret = secret

    @staticmethod
    def from_encoded(encoded: str) -> 'StoragePassword':
        """
        Creates a StoragePassword object from an encoded password.
        :param encoded: The encoded password.
        :return: The StoragePassword object.
        """
        decoded = base58.b58decode(encoded).decode('utf-8')
        try:
            secret, index = decoded.split(JOINER)
            return StoragePassword(int(index), secret)
        except ValueError:
            raise ValueError('Invalid password')

    @staticmethod
    def generate(index: int, secret_length: int = 6) -> 'StoragePassword':
        """
        Generate a random password.
        :param index: The index of the password.
        :param total: The total number of passwords.
        :param secret_length: The length of the password.
        :return: The StoragePassword object.
        """
        secret = ''.join(secrets.choice(ascii_uppercase + digits) for _ in range(secret_length))
        return StoragePassword(index, secret)

    @property
    def decoded(self) -> str:
        """
        Get the decoded password.
        :return: The decoded password.
        """
        return JOINER.join([self.secret, str(self.index)])

    @property
    def encoded(self: str) -> str:
        """
        Get the encoded password.
        :return: The encoded password.
        """
        return base58.b58encode(self.decoded).decode('utf8')
