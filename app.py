from flask import Flask
from services.weather_service import get_weather
app = Flask(__name__)

@app.route("/")
def home():
    weather_data = get_weather("Chandigarh")
    if "error" in weather_data:
        return f"Error: {weather_data['error']}"
    return f"""
    <h1>WeatherPulse</h1>
    <h2>City: {weather_data['city']}</h2>
    <h3>Country: {weather_data['country']}</h3>
    <hr>
    <p>Sunrise: {weather_data['sunrise']}</p>
    <p>Sunset: {weather_data['sunset']}</p>
    <p>Temperature: {weather_data['temperature_celsius']}°C</p>
    <p>Feels Like: {weather_data['feels_like']} °C</p>
    <p>Minimum Temperature: {weather_data['minimum_temperature']}°C</p>
    <p>Maximum Temperature: {weather_data['maximum_temperature']}°C</p>
    <p>Humidity: {weather_data['humidity']}%</p>
    <p>Pressure: {weather_data['pressure']} hPa</p>
    <p>Weather Condition: {weather_data['weather_condition']}</p>
    <p>Description: {weather_data['weather_description']}</p>
    <p>Wind Speed: {weather_data['wind_speed']} m/s</p>"""

if __name__=="__main__":
    app.run(debug=True)
