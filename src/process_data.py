import pandas as pd

def process_weather(data):
    """Convert JSON weather response into a DataFrame."""
    processed = {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Feels Like (°C)": data["main"]["feels_like"],
        "Humidity (%)": data["main"]["humidity"],
        "Pressure (hPa)": data["main"]["pressure"],
        "Wind Speed (m/s)": data["wind"]["speed"],
        "Condition": data["weather"][0]["description"]
    }
    return pd.DataFrame([processed])
