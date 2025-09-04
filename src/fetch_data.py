import requests
import os

API_KEY = "Your_API_key"  # Store key in environment variable

def fetch_weather(city="London", units="metric"):
    """Fetch current weather data for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.json()}")
    return response.json()
