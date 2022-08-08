import requests
from twilio.rest import Client  # Twilio is being a bitch so i can't use it


# Online JSON Viewer = http://jsonviewer.stack.hu/

API_KEY = "fc1eb0877d58355fa4e76dfd681df497"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "1234567890"
auth_token = "0987654321"

parameters = {
    # Dakar (Sunny)
    # "lat": 14.716677,
    # "lon": -17.467686,

    # Vancouver (Rainy)
    # "lat": 49.282730,
    # "lon": -123.120735,

    # Manila (Default)
    "lat": 14.6042,
    "lon": 120.9822,

    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(OWM_Endpoint, params=parameters)
data = response.json()

weather_slice = weather_id = data["hourly"][0:11]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from='+639151754150',
        to='+639173169222'
    )
    print(message.status)


