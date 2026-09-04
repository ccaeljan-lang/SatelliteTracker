import os
from dotenv import load_dotenv
from n2yo import N2YO

load_dotenv()

API_KEY = os.getenv("API_KEY")

n2yo = N2YO(API_KEY)

data = n2yo.get_tle(45217)

print(data["info"]["satname"])
print(data["tle"])
