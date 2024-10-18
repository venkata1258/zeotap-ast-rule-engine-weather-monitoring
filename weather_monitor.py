import requests
from datetime import datetime

# Your OpenWeatherMap API key (replace with your actual key)
API_KEY = 'fc955a604ad4729023ff9753d3be186f'
# The base URL for fetching weather data
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def get_weather_data(city):
    # Construct the complete URL for the city
    url = BASE_URL.format(city, API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data for {city}.")
        return None

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data, temp_unit):
    if data:
        temp_kelvin = data['main']['temp']
        
        # Convert based on user preference
        if temp_unit == 'C':
            temp = kelvin_to_celsius(temp_kelvin)
            temp_label = "°C"
        else:
            temp = temp_kelvin
            temp_label = "K"  # Kelvin

        weather = data['weather'][0]['main']
        timestamp = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')

        city = data['name']  # Get the city name from the API response

        print(f"\nCity: {city}")
        print(f"Temperature: {temp:.2f}{temp_label}")
        print(f"Weather Condition: {weather}")
        print(f"Data Retrieved At: {timestamp}")

def main():
    # Ask the user for the city name
    city = input("Enter the city name: ").strip().capitalize()
    
    # Ask the user for their preferred temperature unit
    temp_unit = input("Choose temperature unit (C for Celsius, K for Kelvin): ").strip().upper()

    # Validate user input
    if temp_unit not in ['C', 'K']:
        print("Invalid input. Defaulting to Celsius.")
        temp_unit = 'C'

    # Fetch and process weather data for the input city
    weather_data = get_weather_data(city)
    if weather_data:
        process_weather_data(weather_data, temp_unit)

if __name__ == "__main__":
    main()
