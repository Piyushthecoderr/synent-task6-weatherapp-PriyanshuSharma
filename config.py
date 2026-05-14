import os
from dotenv import load_dotenv
load_dotenv()
weather_api_key=os.getenv("API_KEY")
BASE_URL="https://api.openweathermap.org/data/2.5/weather"