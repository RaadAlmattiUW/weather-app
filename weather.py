

def get_weather(city):
    api_key = 'ab6bf3d194c0488f951232959242507'  # Replace with your actual API key from OpenWeatherMap
    base_url = "https://www.weatherapi.com/my/"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()

    print(data)  # Print the entire JSON response for debugging

    if response.status_code == 200:  # HTTP status code 200 means OK
        if "main" in data:
            main = data["main"]
            weather = data["weather"]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            weather_description = weather[0]["description"]
            
            print(f"Temperature: {temperature}")
            print(f"Atmospheric pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Weather description: {weather_description}")
        else:
            print("Error: 'main' key not found in the response.")
    else:
        print(f"Error: Unable to fetch weather data. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
