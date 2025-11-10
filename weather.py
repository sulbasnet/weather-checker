import requests

def weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()

            area = data['nearest_area'][0]['areaName'][0]['value']
            region = data['nearest_area'][0]['region'][0]['value']
            country = data['nearest_area'][0]['country'][0]['value']
            temperature = data['current_condition'][0]['temp_C']
            weather_info = data['current_condition'][0]['weatherInfo'][0]['value']
            humidity = data['current_condition'][0]['humidity']

            print(f"\nWeather Report for {area}, {region}, {country}")
            print("-------------------------------------------")
            print(f"Temperature : {temperature}°C")
            print(f"Weather     : {weather_info}")
            print(f"Humidity    : {humidity}%")

        else:
            print("Unable to fetch weather data. Please try again.")
    
    except requests.exceptions.RequestException as e:
        print("Network error occurred:", e)
    except (KeyError, IndexError):
        print("Couldn't get the weather data correctly.")


def main():
    print("Welcome to Python Weather Checker!")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Have a great day!")
            break
        elif city:
            weather(city)
        else:
            print("Please enter a valid city name.")


if __name__ == "__main__":
    main()
