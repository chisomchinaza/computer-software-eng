# weather_cli.py

import requests  # Library for making HTTP requests
import argparse  # Library for handling command-line arguments
import sys       # For handling potential errors more gracefully

def get_arguments():
    parser = argparse.ArgumentParser(description="Get the current weather for a city.")
    parser.add_argument("city", type=str, help="The city name to get weather for.")
    return parser.parse_args()

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse JSON data
        return data
    else:
        print("Failed to retrieve data. Please check the city name or your API key.")
        sys.exit(1)

def display_weather(data):
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    
    print(f"Weather in {city}:\nTemperature: {temperature}°C\nDescription: {description.capitalize()}")

if __name__ == "__main__":
    args = get_arguments()
    api_key = "e68afe79bd2c1fda1e84e9373a665d8a" 
    data = get_weather(args.city, api_key)
    display_weather(data)
