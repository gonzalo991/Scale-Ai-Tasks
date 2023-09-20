'''
import requests

# Your AccuWeather API key
api_key = 'YOUR_API_KEY'

# List of locations
locations = [
    {"city": "New York", "country": "USA"},
    {"city": "Paris", "country": "France"},
    {"city": "London", "country": "UK"}
]

# Fetch the location key for the given city and country
def get_location_key(api_key, city, country):
    location_url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": api_key,
        "q": f"{city},{country}",
    }
    
    try:
        response = requests.get(location_url, params=params)
        response.raise_for_status()
        location_data = response.json()
        location_key = location_data[0]["Key"]
        return location_key
    except requests.exceptions.RequestException as e:
        print(f"Error fetching location key: {e}")
        return None

# Fetch current weather data using the location key
def get_current_weather(api_key, location_key):
    current_weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
    params = {
        "apikey": api_key,
    }
    
    try:
        response = requests.get(current_weather_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data[0]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current weather data: {e}")
        return None

# Main program
if __name__ == "__main__":
    for location in locations:
        city = location["city"]
        country = location["country"]
        location_key = get_location_key(api_key, city, country)
        if location_key:
            weather_data = get_current_weather(api_key, location_key)
            if weather_data:
                temperature_celsius = weather_data["Temperature"]["Metric"]["Value"]
                weather_text = weather_data["WeatherText"]
                print(f"Weather in {city}, {country}:")
                print(f"Temperature (Celsius): {temperature_celsius}")
                print(f"Weather: {weather_text}")
                print()
            else:
                print(f"Unable to fetch weather data for {city}, {country}.")
        else:
            print(f"Unable to fetch location key for {city}, {country}.")
'''

import requests
import time

# Definir la clave de la API y la URL base
api_key = 'YOUR_API_KEY'
base_url = 'https://dataservice.accuweather.com/currentconditions/v1/'

# Definir las ubicaciones
locations = {
    'New York': '349727',
    'Paris': '623',
    'London': '328328'
}

# Función para obtener el clima actual
def get_current_weather(location_key):
    try:
        url = f'{base_url}{location_key}?apikey={api_key}'
        response = requests.get(url)
        response.raise_for_status()  # Generar una excepción si la respuesta no es exitosa
        data = response.json()
        return data[0] if data else None
    except requests.exceptions.RequestException as e:
        print(f'Error en la solicitud HTTP: {e}')
    except Exception as e:
        print(f'Error: {e}')
    return None

# Función para mostrar el clima
def display_weather(location, weather_data):
    if weather_data:
        print(f'Condiciones climáticas en {location}:')
        print(f'Temperatura: {weather_data["Temperature"]["Metric"]["Value"]}°C')
        print(f'Tiempo: {weather_data["WeatherText"]}')
    else:
        print(f'No se pudo obtener el clima para {location}')

# Bucle para actualizar el clima cada 5 minutos
while True:
    for location, location_key in locations.items():
        weather_data = get_current_weather(location_key)
        display_weather(location, weather_data)
    time.sleep(300)  # Esperar 5 minutos antes de la siguiente actualización
