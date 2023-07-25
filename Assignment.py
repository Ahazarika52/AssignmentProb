import requests


API_KEY = "b6907d289e10d714a6e88b30761fae22" 
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"


def get_weather_data(date):
    try:
        params = {
            "q": "London,us",
            "appid": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        for entry in data['list']:
            if entry['dt_txt'].startswith(date):
                print(f"Temperature on {entry['dt_txt']}: {entry['main']['temp']}°C")
                return
        
        print("No data available for the given date.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)


def get_wind_speed(date):
    try:
        params = {
            "q": "London,us",
            "appid": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        for entry in data['list']:
            if entry['dt_txt'].startswith(date):
                print(f"Wind Speed on {entry['dt_txt']}: {entry['wind']['speed']} m/s")
                return

        print("No data available for the given date.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)


def get_pressure(date):
    try:
        params = {
            "q": "London,us",
            "appid": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        for entry in data['list']:
            if entry['dt_txt'].startswith(date):
                print(f"Pressure on {entry['dt_txt']}: {entry['main']['pressure']} hPa")
                return

        print("No data available for the given date.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)


def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_weather_data(date)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_wind_speed(date)
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_pressure(date)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
