import requests
import json
import sys

API_KEY = 'YOUR_API_KEY' # Replace with your API key

def get_weather_forecast(city):
    """
    Fetches the weather forecast for a given city.
    Handle exceptions and errors using try-except block
    Args:
        city (str): The name of the city.
    Returns:
        dict: The weather forecast data as a dictionary after storing it in weather_data variable.
    """
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    complete_url = base_url + city + '&appid=' + API_KEY
    try:
        response = requests.get(complete_url)
        weather_data = response.json()
        return weather_data
    except Exception as e:
        print("Error occurred while fetching weather forecast for {}: {}".format(city, e))
        sys.exit(1)

def parse_weather_data(weather_data):
    """
    Parses the weather forecast data and extracts relevant information like city name, temperature, pressure, weather description, wind speed and humidity.
    Args:
        weather_data (dict): The weather forecast data as a dictionary.
    Returns:
        dict: The parsed weather information.
    """
    if weather_data['cod'] == 200:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        pressure = weather_data['main']['pressure']
        weather_desc = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']
        weather_info = {
            'city': city,
            'temperature': round(temperature - 273.15, 2),
            'pressure': pressure,
            'weather_desc': weather_desc,
            'wind_speed': wind_speed,
            'humidity': humidity
        }
        return weather_info
    else:
        print("Error occurred while fetching weather forecast : {}".format(weather_data['message']))
        sys.exit(1)

def display_weather_forecast(weather_forecast):
    """
    Displays the weather forecast information.
    Args:
        weather_forecast (dict): The parsed weather forecast data.
    """
    print("Weather forecast for {}:".format(weather_forecast['city']))
    print("Temperature: {} C".format(weather_forecast['temperature']))
    print("Pressure: {} hPa".format(weather_forecast['pressure']))
    print("Weather Description: {}".format(weather_forecast['weather_desc']))
    print("Wind Speed: {} m/s".format(weather_forecast['wind_speed']))
    print("Humidity: {}%".format(weather_forecast['humidity']))

def main():
    """
    The main function to drive the program.
    Handle exceptions related to no command line argument using try-except block
    Args:
        city_name(string): Take the input for the city name from the command line and parse that argument
    """
    try:
        city_name = sys.argv[1]
    except Exception as e:
        print("Error occurred while fetching weather forecast for {}: {}".format(city_name, e))
        sys.exit(1)
    weather_data = get_weather_forecast(city_name)
    weather_forecast = parse_weather_data(weather_data)
    display_weather_forecast(weather_forecast)

if __name__ == '__main__':
    main()