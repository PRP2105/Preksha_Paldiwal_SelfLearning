import requests

def fetch_weather_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"

    try:
        response = requests.get(url, timeout=10)
        
        response.raise_for_status()
        
        data = response.json()
        
        current_weather = data.get('current_weather', {})
        temperature = current_weather.get('temperature')
        windspeed = current_weather.get('windspeed')
        weathercode = current_weather.get('weathercode')
        timezone = data.get('timezone', 'Unknown')
        
        summary = (
            f"--- Weather Report ---\n"
            f"Location: Latitude {lat}, Longitude {lon}\n"
            f"Timezone: {timezone}\n"
            f"Temperature: {temperature}°C\n"
            f"Windspeed: {windspeed} km/h\n"
            f"Weathercode: {weathercode}\n"
            f"----------------------\n"
        )
        
        with open("weather_report.txt", "w", encoding="utf-8") as file:
            file.write(summary)
            
        print("Success: Weather data fetched and saved to weather_report.txt")
        
    except requests.exceptions.Timeout:
        print("Error: The connection timed out.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred (Status code not 200): {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Network error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")

if __name__ == "__main__":
    fetch_weather_data(18.0760, 74.8777)