import requests
import argparse
import os
from datetime import datetime

API_KEY = os.environ.get("WWO_API_KEY", "your_api_key_here")
BASE_URL = "https://api.worldweatheronline.com/premium/v1/weather.ashx"

WEATHER_ICONS = {
    "sunny": "☀", "clear": "🌙", "partly cloudy": "⛅",
    "cloudy": "☁", "overcast": "☁", "mist": "🌫",
    "fog": "🌫", "rain": "🌧", "drizzle": "🌦",
    "snow": "❄", "sleet": "🌨", "thunder": "⛈", "blizzard": "🌨",
}

def get_icon(description):
    desc = description.lower()
    for keyword, icon in WEATHER_ICONS.items():
        if keyword in desc:
            return icon
    return "🌡"

def get_weather(location, days=5):
    if API_KEY == "your_api_key_here":
        print("❌ Set your API key: export WWO_API_KEY='your_key'")
        print(" Get one free: https://www.worldweatheronline.com/weather-api/")
        return None
    params = {
        "key": API_KEY, "q": location, "format": "json",
        "num_of_days": days, "tp": 24, "includelocation": "yes", "cc": "yes",
    }
    try:
        r = requests.get(BASE_URL, params=params, timeout=10)
        r.raise_for_status()
        data = r.json().get("data", {})
        if "error" in data:
            print(f"❌ {data['error'][0]['msg']}")
            return None
        return data
    except requests.exceptions.ConnectionError:
        print("❌ No internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
    return None

def display_current(current, location_name):
    desc = current["weatherDesc"][0]["value"]
    icon = get_icon(desc)
    print("\n" + "─" * 50)
    print(f"📍 {location_name} — Right Now")
    print("─" * 50)
    print(f"{icon} {desc}")
    print(f"🌡 Temperature : {current['temp_C']}°C / {current['temp_F']}°F (Feels like {current['FeelsLikeC']}°C)")
    print(f"💧 Humidity : {current['humidity']}%")
    print(f"💨 Wind : {current['windspeedMiles']} mph {current['winddir16Point']}")
    print(f"👁 Visibility : {current['visibility']} km")
    print(f"☀ UV Index : {current['uvIndex']}")
    print("─" * 50)

def display_forecast(weather_days):
    print("\n📅 Forecast\n")
    print(f"{'Date':<14} {'Conditions':<25} {'High':>7} {'Low':>7} {'Rain%':>7} {'Wind':>7}")
    print("─" * 75)
    for day in weather_days:
        date_fmt = datetime.strptime(day["date"], "%Y-%m-%d").strftime("%a %d %b")
        desc = day["hourly"][0]["weatherDesc"][0]["value"]
        icon = get_icon(desc)
        rain = day["hourly"][0].get("chanceofrain", "N/A")
        wind = day["hourly"][0]["windspeedMiles"]
        print(f"{date_fmt:<14} {icon+' '+desc:<25} {day['maxtempC']+'°C':>7} {day['mintempC']+'°C':>7} {rain+'%':>7} {wind:>7}")
    print("─" * 75)

def main():
    parser = argparse.ArgumentParser(description="World Weather Online — Terminal Dashboard")
    parser.add_argument("--location", "-l", default="London")
    parser.add_argument("--days", "-d", type=int, default=5)
    args = parser.parse_args()

    print(f"\n🌍 Fetching weather for {args.location}...")
    data = get_weather(args.location, args.days)
    if not data:
        return

    try:
        area = data["nearest_area"][0]["areaName"][0]["value"]
        country = data["nearest_area"][0]["country"][0]["value"]
        location_name = f"{area}, {country}"
    except (KeyError, IndexError):
        location_name = args.location

    display_current(data["current_condition"][0], location_name)
    display_forecast(data["weather"])
    print("\nData by World Weather Online — https://www.worldweatheronline.com\n")

if __name__ == " __main__":
    main()
# It's Developed with love by Zioles(Dhrruv).
