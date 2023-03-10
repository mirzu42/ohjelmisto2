import requests
import json


class pyynto():
    kaupunki = input(("Syötä haluamasi kaupunki: "))
    pyynto1 = "http://api.openweathermap.org/geo/1.0/direct?q=" + kaupunki + "&limit=&appid=f41f98e18b62d8ae9e7fba911e962a0c"
    lat, lon = "", ""

    try:
        vastaus = requests.get(pyynto1)
        if vastaus.status_code == 200:
            jsonVastaus = vastaus.json()
            lat = jsonVastaus[0]["lat"]
            lon = jsonVastaus[0]["lon"]
        pyynto2 = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(
            lon) + "&appid=f41f98e18b62d8ae9e7fba911e962a0c&units=metric"
        vastaus2 = requests.get(pyynto2)
        if vastaus2.status_code == 200:
            jsonVastaus2 = vastaus2.json()
            # print (json.dumps(jsonVastaus2, indent=2))
            print("Kuvaus: " + str(jsonVastaus2["weather"][0]["description"]))
            print("Lämpötila: " + str(jsonVastaus2["main"]["temp"]) + " Celcius astetta")




    except requests.exceptions.RequestException as e:
        print("Jokin meni vikaan")


class main():
    pyynto()
