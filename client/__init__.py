import requests


from .AclEntry import AclEntry

from .client import Client as APIClient


class Client:
    def __init__(self, base_uri="https://127.0.0.1:5000"):
        self.api = APIClient(base_uri)
        