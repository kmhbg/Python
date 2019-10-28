class Bet:

    def __init__(self, name, amount, posOne, posTwo, posThree):
        self. name = name
        self.amount = amount
        self.posOne = posOne
        self.posTwo = posTwo
        self.posThree = posThree


import requests
import json
BASE_URL = 'http://ergast.com/api/f1'


def get_race_results():
    url = "%s/current/last/results.json"%(BASE_URL)
    r = requests.get(url)
    final = []
    if r.status_code == 200:
        
        json_data = json.loads(r.text)
        for i in json_data["MRData"]["RaceTable"]["Races"][0]["Results"]:
            final.append(i["position"] + ": " + i["Driver"]["givenName"] + " " + i["Driver"]["familyName"] + " Team: " + i["Constructor"]["name"])
            
    else:
        print("Error " + str(r.status_code))
        return False
    return final
    



print(get_race_results()[1])
