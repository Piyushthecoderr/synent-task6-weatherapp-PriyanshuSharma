# WeatherPulse 🌦️
WeatherPulse is a responsive weather web application built using Flask and OpenWeatherMap API.  
It provides real-time weather information with dynamic weather-based backgrounds and modern UI.

## Features
- Real-time weather data
- Dynamic weather backgrounds
- Responsive mobile-friendly UI
- Weather icons
- Recent city searches using Flask sessions
- Error handling
- Secure API key management using `.env`

## Tech Stack
- Python
- Flask
- HTML
- CSS
- JavaScript
- OpenWeatherMap API

## Setup

### Clone Repository
```bash
git clone <your_repository_url>
cd WeatherPulse
```

### Create Virtual Environment
```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)
```bash
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create `.env` File
```env
API_KEY=your_openweathermap_api_key
SECURE_KEY=your_secret_key
```

### Run Application
```bash
python app.py
```

### Open In Browser
```text
http://127.0.0.1:5000
```

### Future Improvements
- 5-day weather forecast
- Current location weather
- Dark/light theme toggle
- Search suggestions
- Animated weather effects