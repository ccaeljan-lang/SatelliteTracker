import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://api.n2yo.com/rest/v1/satellite/tle/45217/&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

satellite_name = data["info"]["satname"]
satellite_id = data["info"]["satid"]

tle = data["tle"]

print("Satellite:", satellite_name)
print("NORAD ID:", satellite_id)
print("TLE:")
print(tle)
