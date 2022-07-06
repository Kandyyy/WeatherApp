import requests
from datetime import datetime

class Weather:
    def __init__(self,url: str) -> None:
        self.url = url
    
    def getWeather(self) -> list:
        response = requests.get(self.url)
        json_response = response.json()
        cardContent = [str("{:.1f}\N{DEGREE SIGN}C".format(json_response["main"]["temp"]-273.15)),json_response["weather"][0]["description"],json_response["weather"][0]["icon"],datetime.now().time().strftime("%H:%M")]
        return cardContent

