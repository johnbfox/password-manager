from abc import ABC, abstractmethod
import os
import random
import string
from cryptography.fernet import Fernet


class PasswordBackend(ABC):
    def save(self, key, value):
        pass

    def get(self, key):
        pass


class PasswordFilesystemBackend(object):
    def __init__(self, root=os.path.expanduser('~')):
        self.root = root
        self.password_dir = os.path.join(root, ".passwords")

        if not os.path.exists(self.password_dir):
            os.makedirs(self.password_dir)

        config_file = os.path.join(root, ".passwordsrc")

        if not os.path.exists(config_file):
            key = Fernet.generate_key().decode('utf-8')
            with open(config_file, "w+") as f:
                f.write(key)

        with open(config_file, "r") as f:
            self.key = f.readline()
            self.fernet = Fernet(self.key)

    def save(self, key, value):
        """
        Creates or overwrites password of name "key" with value
        """

        with open(os.path.join(self.password_dir, key), "w+") as f:
            encryted_data = self.fernet.encrypt(bytes(value, "utf-8"))
            f.write(encryted_data.decode("utf-8"))

    def get(self, key):
        if not os.path.exists(os.path.join(self.password_dir, key)):
            return None
        
        with open(os.path.join(self.password_dir, key), "r") as f:
            return self.fernet.decrypt(bytes(f.readline(), "utf-8"))
