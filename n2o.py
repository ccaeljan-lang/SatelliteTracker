import requests


class N2YO:
    BASE_URL = "https://api.n2yo.com/rest/v1/satellite"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_tle(self, satellite_id):
        url = f"{self.BASE_URL}/tle/{self.satellite_id}"

        params = {
            "apiKey": self.api_key
        }

        response = requests.get(url, params=params)

        response.raise_for_status()

        return response.json()
