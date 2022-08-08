import requests
from datetime import datetime

MY_LAT = 14.599512
MY_LONG = 120.984222

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Status Codes
# 200 = Its okay
# 4XX = It fucked up
# 401 = Unauthorized access
# 404 = It doesn't exist

# ------ Status Codes ------ #
# if response.status_code == 404:
#     raise Exception("Resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access.")

# response.raise_for_status()
# # data = response.json()
# # data = response.json()["iss_position"]
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)


# ------ Parameters ------ #
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# print(sunrise)
print(sunrise.split("T")[1].split(":")[0])  # Split index 0 by T and index 1 by :
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)



