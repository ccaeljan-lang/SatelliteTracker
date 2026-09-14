import os
# import matplotlib.pyplot as plt
import plotly.graph_objects as go
# from time_n2yo import convertTime
from dotenv import load_dotenv
from n2yo import N2YO

load_dotenv()

API_KEY = os.getenv("API_KEY")

n2yo = N2YO(API_KEY)

observer_latitude = 14.5631516
observer_longitude = 120.9848638
observer_altitude = 13

data = n2yo.get_positions(
    45217,
    observer_latitude,
    observer_longitude,
    observer_altitude,
    60
)

positions = data["positions"]

latitudes = [position["satlatitude"]
             for position in positions]

longitudes = [position["satlongitude"]
              for position in positions]

fig = go.Figure()

fig.add_trace(
    go.Scattergeo(
        lat=latitudes,
        lon=longitudes,
        mode="lines+markers",
        name="ISS"
    )
)

fig.update_layout(
    title="ISS Ground Track",
    geo=dict(
        showland=True,
        showcountries=True
    )
)

fig.show()

# SIMPLE PLOT
# plt.plot(longitudes, latitudes)

# plt.xlabel("Longitude")
# plt.ylabel("Latitude")

# plt.title("Satellite Ground Track")

# plt.show()

# SIMPLE DATA DISPLAY
# print(f"Satellite Name: {data["info"]["satname"]}")
# print(f"Satellite ID: {data["info"]["satid"]}")
# print("=" * 30)

# for position in data["positions"]:
#     print(f"Latitude: {position['satlatitude']:.2f}°")
#     print(f"Longitude:: {position['satlongitude']:.2f}°")
#     print(f"Altitude:: {position['satlatitude']:.2f}°")
#     print(f"Azimuth:: {position['azimuth']:.2f}°")
#     print(f"Elevation:: {position['elevation']:.2f}°")
#     print(f"Time: {convertTime(position['timestamp'])}")
#     print("-" * 30)
