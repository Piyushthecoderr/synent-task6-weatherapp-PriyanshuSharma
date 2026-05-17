from flask import Flask,render_template,request,session
from services.weather_service import get_weather
from configuration import SECRET_KEY

app=Flask(__name__)
app.secret_key=SECRET_KEY
@app.route("/",methods=["GET", "POST"])
def home():
    weatherData = None
    if "recent_searches" not in session:
        session["recent_searches"]=[]

    if request.method=="POST":
        cityName=request.form.get("city")
        weatherData=get_weather(cityName)
        if "error" not in weatherData:
            fetch_recent_search=session["recent_searches"]
            if cityName not in fetch_recent_search:
                fetch_recent_search.insert(0,cityName)
                session["recent_searches"]=fetch_recent_search[:5]

    backgClass="weatherDefault"
    if weatherData and "error" not in weatherData:
        weather_condition=weatherData["weather_condition"].lower()
        if "cloud" in weather_condition:
            backgClass="weatherCloudy"

        elif "rain" in weather_condition:
            backgClass="weatherRainy"

        elif "clear" in weather_condition:
            backgClass="weatherClear"

        elif "snow" in weather_condition:
            backgClass="weatherSnowy"

        elif "thunderstorm" in weather_condition:
            backgClass="weatherStormy"

    return render_template("index.html",weather_data=weatherData,recent_searches=session["recent_searches"],background_class=backgClass)

if __name__=="__main__":
    app.run(debug=True)
