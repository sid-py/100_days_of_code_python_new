import requests
import smtplib

api_key = "39694ab1cb0d435fd52fef3d79091bb2"

MY_EMAIL = "progc515@gmail.com"
MY_PASSWORD = "pyThon1986$$"

parameters = {
    "lat": "47.736389",
    "lon":"8.969160",
    "appid":api_key,
    "exclude":"current,minutely,daily",   
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params = parameters)
response.raise_for_status()
data = response.json()
# twelve_hr_weather_data = data["hourly"][0]["weather"][0]["id"]
weather_slice = data["hourly"][:12]

will_rain =  False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
       
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASSWORD)
            connection.sendmail(from_addr = MY_EMAIL, to_addrs = "siddhesh.sule47@gmail.com", msg = f"Subject: Weather update of the Day!\n\nIt will rain today. Carry an Umbrella.")     
    
