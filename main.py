import os
from dotenv import load_dotenv
from n2yo import N2YO

load_dotenv()

API_KEY = os.getenv("API_KEY")

n2yo = N2YO(API_KEY)

data = n2yo.get_positions(
    satellite_id=25544,
    latitude=14.5995,
    longitude=120.9842,
    altitude=10,
    seconds=10
)

print(f"Satellite Name: {data["info"]["satname"]}")
print(f"Satellite ID: {data["info"]["satid"]}")
print("=" * 30)

for position in data["positions"]:
    print(f"Latitude: {position['satlatitude']:.2f}°")
    print(f"Longitude:: {position['satlongitude']:.2f}°")
    print(f"Altitude:: {position['satlatitude']:.2f}°")
    print(f"Azimuth:: {position['azimuth']:.2f}°")
    print(f"Elevation:: {position['elevation']:.2f}°")
    print("-" * 30)
