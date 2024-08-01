weather_data = { 
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, 
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} 
} 

#Welcome Message: Display a welcome message to the user.
def welcome_message():
    print("Welcome to this Weather App!")

#User Input: Ask for the city name for which the weather forecast is needed. 
def get_city_name():
    return input("Please enter the name of your city: ")

#Fetch Weather Data: Use hardcoded weather data for several cities to simulate fetching weather information. 
def display_weather_data(city):
    data = weather_data[city]
    print(f"weather forecast for {city}:")
    print(f"temperature: {data['temperature']}")
    print(f"conditions: {data['conditions']}")
    print(f"wind speed: {data['wind_speed']}")
    print(f"humidity: {data['humidity']}")


#Data Validation: Ensure valid input by checking that the user enters a valid city name from the hardcoded list. 
def validate_city(city):
    return city in weather_data

#Thank You Message: Thank the user for using the weather forecast application. 
def thank_you_message():
    print("Thank you for using this weather App!")

def app():
    welcome_message()

    while True:
        city = get_city_name()
        if validate_city(city):
            display_weather_data(city)
            break
        else:
            print("please choose a valid city")
    thank_you_message()

if __name__ == "__main__":
    app()