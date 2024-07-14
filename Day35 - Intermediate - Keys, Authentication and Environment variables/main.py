import requests
from twilio.rest import Client

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "__YOUR_OWM_API_KEY__"  # use you own api key
# api_key = os.environ.get("API_KEY")  # using pythonanywhere and environment variables to hide api key
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"  # use your own account sid from twilio
# account_sid = os.environ.get("ACCOUNT_SID")  # using pythonanywhere and environment variables to hide account sid
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"  # use your own auth token from twilio
# auth_token = os.environ.get("AUTH_TOKEN")  # using pythonanywhere and environment variables to hide auth token

weather_params = {
    "lat": 27.717245,
    "lon": 85.323959,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for every_hour in weather_data["list"]:
    condition_code = int(every_hour["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is likely to rain today. It is suggested to  bring an umbrella ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",  # use your own twilio virtual number
        to="YOUR TWILIO VERIFIED REAL NUMBER"  # use your own verified real number in twilio
    )
    print(message.status)

