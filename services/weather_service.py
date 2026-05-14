import requests
from datetime import datetime
from config import weather_api_key,BASE_URL
def get_weather(city_name):
    #URL query parameters.
    params={ 
        "q":city_name, #Used by OpenWeatherMap to know: which city weather requested.
        "appid":weather_api_key,
        "units":"metric" #metric → Celsius,imperial → Fahrenheit,(no units) → Kelvin
        }

    try:
        ## response is a special Response object created by requests library.It contains status code, headers, JSON data, etc.
        response = requests.get(BASE_URL, params=params)
        #Server returns data in JSON format.Converts JSON response into Python dictionary
        data = response.json()
        # | Status Code | What it Implies        |
        # |-------------| ---------------------- |
        # |    200      | Request Successful     |
        # |    404      | Request City not found |
        # |    401      | Invalid API key        |

        if response.status_code!=200:
        # Tries to get value of "message" key.If key not found then it returns "Something went wrong"
            return { "error":data.get("message","Something didn't went Correctly")}
        
        weather_details={
        "city":data["name"],
            
        #Sys: System/internal information section,Contains:country,sunrise,sunset
            "country":data["sys"]["country"],
            "sunrise":datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
            "sunset":datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p"),

        #For grouping related weather measurements together.Inside "main":temp,humidity,pressure,feels_like,temp_min,temp_max
            "temperature_celsius":data["main"]["temp"],
            "feels_like":data["main"]["feels_like"],
            "minimum_temperature":data["main"]["temp_min"],
            "maximum_temperature":data["main"]["temp_max"],
            "humidity":data["main"]["humidity"],
            "pressure":data["main"]["pressure"],

        "weather_condition":data["weather"][0]["main"],
        "weather_description":data["weather"][0]["description"],

        "wind_speed":data["wind"]["speed"]
        }

        return weather_details

    except Exception as error:
        return { "error": str(error)}