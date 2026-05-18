def getBackgroundClass(weather_condition):
    weather_condition=weather_condition.lower()

    if "cloud" in weather_condition:
        return "weatherCloudy"

    elif "rain" in weather_condition:
        return "weatherRainy"

    elif "clear" in weather_condition:
        return "weatherClear"

    elif "snow" in weather_condition:
        return "weatherSnowy"

    elif "thunderstorm" in weather_condition:
        return "weatherStormy"
    
    elif ("haze" in weather_condition or "mist" in weather_condition or "fog" in weather_condition or "smoke" in weather_condition):
        return "weatherHaze"

    return "weatherDefault"