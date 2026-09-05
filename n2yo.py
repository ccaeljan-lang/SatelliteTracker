import requests


class N2YO:
    BASE_URL = "https://api.n2yo.com/rest/v1/satellite"

    # constructor for N2YO object
    def __init__(self, api_key):
        # stores api key from .env file
        self.api_key = api_key

    # method to get tle data
    def get_tle(self, satellite_id):
        # formatted url including satellite id
        url = f"{self.BASE_URL}/tle/{satellite_id}"

        # struct of api key
        params = {
            "apiKey": self.api_key
        }

        # response request to get tle data
        response = requests.get(url, params=params)

        # check status
        response.raise_for_status()

        # return tle data in json form
        return response.json()

    # methods to get positions
    def get_positions(self, satellite_id, latitude, longitude, altitude, seconds):
        # formatted url with other stuffs
        url = (
            f"{self.BASE_URL}/tle/{satellite_id}/"
            f"{latitude}/"
            f"{longitude}/"
            f"{altitude}/"
            f"{seconds}"
        )

        params = {
            "apiKey": self.api_key
        }

        # response request to get tle data
        response = requests.get(url, params=params)

        # check status
        response.raise_for_status()

        # return tle data in json form
        return response.json()
