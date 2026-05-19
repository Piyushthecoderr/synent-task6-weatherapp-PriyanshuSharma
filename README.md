# WeatherPulse 🌦️
A real-time weather application with dynamic condition based backgrounds and responsive UI,built using Flask and the OpenWeatherMap API.

🔗 **Live Demo:** https://weatherpulse-v8e3.onrender.com
💻 **Tech Stack:** Python,Flask,JavaScript,HTML5,CSS3,Gunicorn,Render

---

## 📸 Preview
### ☀️ Clear Weather
![Clear Weather Preview](static/images/clear-weather-preview.png)

### ☁️ Cloudy Weather
![Cloudy Weather Preview](static/images/cloudy-weather-preview.png)

---

## ⚙️ Architecture & Technical Highlights
* Modular backend structure with dedicated `weather_service.py` for API handling
* Production-ready deployment using Gunicorn on Render
* Secure environment variable management using `.env`
* Robust API error handling with HTTP status validation and exception handling

---

## ✨ Features
* 🌈 Dynamic weather-based backgrounds
* 📱 Fully responsive mobile-friendly UI
* ⚡ Smart UX feedback during API requests
* 🕐 Recent search tracking using Flask sessions
* 🌡️ Real-time weather information with icons and detailed metrics

---

## 🛠️ Local Setup
```bash
git clone https://github.com/Piyushthecoderr/synent-task6-weatherapp-PriyanshuSharma
cd WeatherPulse

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file in the root directory:

```env
API_KEY=your_openweathermap_api_key
SECURE_KEY=your_secret_key
```

Run the application:

```bash
python app.py
```

---

## 🚀 Future Improvements
* Search suggestions
* 5-day weather forecast
* Animated weather effects
* City search autocomplete
* Geolocation based weather