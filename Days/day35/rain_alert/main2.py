import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

account_sid = "<this_is_for_github_twilio_sid>"
auth_token = "<this_is_for_github_twilio_secret_token>"

MY_LAT = 26.607480
MY_LONG = -80.134140

api_key = "this_is_for_github_owm_api_key"

MESSAGE = "It's going to rain today. Remember to bring an umbrella! ☂️"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
   condition_code = hour_data["weather"][0]["id"]
   if int(condition_code) < 700:
      will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=MESSAGE,
        from_="<this_is_for_github_twilio_number>",
        to="<This_is_for_github_number>"
    )
    print(message.sid)
    print(message.status)