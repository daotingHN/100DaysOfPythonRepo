import requests

# PART = "Manila,PH"
API_KEY = "fc1eb0877d58355fa4e76dfd681df497"

# actual_link = "https://api.openweathermap.org/data/2.5/onecall?lat=14.6042&lon=120.9822&appid=fc1eb0877d58355fa4e76dfd681df497"


################ MY ANSWER ################
LAT = 14.6042
LONG = 120.9822
# response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LONG}&appid={API_KEY}")


################ ANGELA's ANSWER ################
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 14.6042,
    "lon": 120.9822,
    "appid": API_KEY
}

response = requests.get(OWM_Endpoint, params=parameters)
# print(response.status_code)
print(response.json())


# Online JSON Viewer = http://jsonviewer.stack.hu/
