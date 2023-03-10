import requests
#import json

pyynto = "https://api.chucknorris.io/jokes/random"
try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        jsonVastaus = vastaus.json()
        print(jsonVastaus["value"])



except requests.exceptions.RequestException as e:
    print("Jokin meni vikaan")


