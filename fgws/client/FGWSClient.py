import requests
from pprint import pprint

class FGWSClient:

    def __init__(self):
        self.base_url = "http://129.79.49.179:5000/"

    def list_active_users(self):
        json_name = "get_active_users.json"
        r = requests.get(self.base_url + json_name)
        res = r.json()
        pprint(res, indent=2)


def list_active_users():
    client = FGWSClient()
    client.list_active_users()
