import requests
from dotenv import load_dotenv

load_dotenv()
import os

RACCOON_BASE_URL = os.getenv("RACCOON_BASE_URL")
RACCOON_SECRET_KEY = os.getenv("RACCOON_SECRET_KEY")
RACCOON_PASSCODE = os.getenv("RACCOON_PASSCODE")


class RaccoonActionModel:
    def __init__(self):
        self.base_url = RACCOON_BASE_URL
        self.headers = {
            'Content-Type': 'application/json',
            'secret-key': RACCOON_SECRET_KEY,
            'raccoon-passcode': RACCOON_PASSCODE
        }

    def pipeline(self, query, app_url, stream):
        payload = {
            "query": query,
            "app_url": app_url,
            "stream": stream
        }

        response = requests.request("POST", self.base_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return {"status_code": response.status_code, "message": "Order placed successfully"}
        else:
            return {"status_code": response.status_code, "message": "Failed to process the request"}
