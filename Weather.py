import requests

class Weather:
    def __init__(self,url: str) -> None:
        self.url = url
    
    def getWeather(self) -> str:
        response = requests.get(self.url)
        json_response = response.json()
        x = json_response["main"]
        temp, humidity, degree_sign = x["temp"], x["humidity"], u'\N{DEGREE SIGN}'
        z= json_response["weather"]
        weather_description = z[0]["description"]
        result="It is " + str("{:.2f}".format(temp-273.15)) + degree_sign + "C" + "," + weather_description + "\nWith a humidity of " + str(humidity) + "%"
        return result