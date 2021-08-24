import requests
from datetime import datetime

MY_LAT = 47.736389
MY_LNG = 8.969160
# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude, longitude)

# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted" : 0,
}
response = requests.get(url ="https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()

sunrise_time = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_time = data["results"]["sunset"].split("T")[1].split(":")[0]
print(data)
print(sunrise_time)
print(sunset_time)
time_now = datetime.now()
print(time_now.hour)