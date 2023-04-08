import requests
import os
from instagram.domain.exceptions import NotDefinedError

class InstagramRequestAPI:
    def __init__(self, endpoint, query_params={}):
        self.endpoint = endpoint
        self.headers = self._get_headers()
        self.query_params = query_params
        self.url = self._get_url_to_request()

    def _get_url_to_request(self):
        api_url = os.environ.get("API_URL")
        if not api_url:
            raise NotDefinedError()
        
        return f"{api_url}/{self.endpoint}"

    def _get_headers(self):
        return {
            "X-RapidAPI-Key": os.environ.get("API_SECRET_KEY"),
            "X-RapidAPI-Host": os.environ.get("API_HOST"),
        }

    def get(self):
        return requests.get(url=self.url, headers=self.headers, params=self.query_params)