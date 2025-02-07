import os
import requests
from dotenv import load_dotenv
from smsSender import rainySMS, sunnySMS

# Cargar las variables del archivo .env
load_dotenv()

# Leer las variables de entorno
MY_EMAIL = os.getenv("MY_EMAIL")
PASSW = os.getenv("PASSW")
api_key = os.getenv("API_KEY")

endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Coordenadas de Madrid
weather_params = {
    "lat": 40.4165,
    "lon": -3.7025,
    "appid": api_key,
    "units": "metric",
    "cnt": 4
}

response = requests.get(url=endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

weather_list = data["list"]
forecast_message = "Pronóstico del tiempo:\n\n"

is_it_rainy = False

for forecast in weather_list:
    if forecast["weather"][0]["id"] < 700:
        is_it_rainy = True

if is_it_rainy:
    rainySMS()
else:
    sunnySMS()
