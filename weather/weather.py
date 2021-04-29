import requests

r = requests.get('https://www.metaweather.com/api/location/2442327')
#print(r.text)
d = r.json()

print("Six day weather forecast for Louisville, KY")
for forecast in d["consolidated_weather"]:
    date = forecast["applicable_date"]
    weather = forecast["weather_state_name"]
    temp = forecast["the_temp"]
    humidity = forecast["humidity"]
    print(f"{date}\tWeather: {weather}\tTemperature: {temp}\tHumidity: {humidity}")
