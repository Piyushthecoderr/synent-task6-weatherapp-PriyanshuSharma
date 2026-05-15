from flask import Flask,render_template,request
from services.weather_service import get_weather
app=Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def home():
    dataWeather=None
    if request.method=="POST":
        cityName=request.form.get("city")
        dataWeather = get_weather(cityName)
    return render_template("index.html",weather_data=dataWeather)

if __name__=="__main__":
    app.run(debug=True)