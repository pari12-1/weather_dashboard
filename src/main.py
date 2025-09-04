from fetch_data import fetch_weather
from process_data import process_weather
from visualize import plot_weather

def main():
    city = input("Enter city name: ")
    print(f"Fetching weather data for {city}...")

    data = fetch_weather(city)
    processed = process_weather(data)
    print(processed)  # Debug: Show raw values in terminal

    plot_weather(processed, city)

if __name__ == "__main__":
    main()
