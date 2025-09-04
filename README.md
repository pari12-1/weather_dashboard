# 🌦️ Weather Dashboard

A simple Python-based weather dashboard that fetches real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/) and visualizes it using Matplotlib & Seaborn.

## 🚀 Features
- Fetches real-time weather data for any city.
- Displays temperature, humidity, pressure, wind speed, and weather condition.
- Creates bar chart visualizations.
- Saves weather plots automatically in the `visuals/` folder.

## 🛠️ Tech Stack
- Python 3.10+
- Requests
- Pandas
- Matplotlib
- Seaborn

## 📂 Project Structure
weather_dashboard/

│── src/

│ ├── fetch_data.py # Fetches data from OpenWeatherMap API

│ ├── process_data.py # Processes and structures the data

│ ├── visualize.py # Creates visualizations

│ ├── main.py # Main entry point

│── visuals/ # Saved plots

│── requirements.txt # Dependencies

│── README.md # Project documentation

│── .gitignore # Ignore unnecessary files


## 🔑 Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/weather_dashboard.git
   cd weather_dashboard

## create virtual environment and install dependencies

python -m venv .venv

source .venv/bin/activate  
# On Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Set up your API key

src/fetch_data.py

API_KEY = "Your_api_key"
## Run the Program

python src/main.py
