from pydantic import BaseModel, Field
from typing import Dict
import requests
import os

class WeatherInput(BaseModel):
    city: str = Field(..., description="City name, e.g. 'Lagos'")

def get_weather(city: str) -> Dict:
    """
    Calls OpenWeather (example). Requires WEATHER_API_KEY in env.
    Replace implementation or API if you already have service.
    """
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return {"error": "WEATHER_API_KEY not set in environment"}
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    res = requests.get(url, params=params)
    if res.status_code != 200:
        return {"error": res.json()}
    j = res.json()
    return {
        "city": city,
        "temperature": j["main"]["temp"],
        "description": j["weather"][0]["description"],
    }
