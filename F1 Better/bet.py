import requests
import json
class Bet:
    totalPot = 0
    


    def __init__(self, name, bet, posOne, posTwo, posThree):
        self. name = name
        self.bet = bet
        self.posOne = posOne
        self.posTwo = posTwo
        self.posThree = posThree
    



    @classmethod
    def get_race_results(self):
        BASE_URL = 'http://ergast.com/api/f1' 
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

    @classmethod
    def getTopThree(self):
        top = Bet.get_race_results()[0] + "\n", Bet.get_race_results()[1] + "\n", Bet.get_race_results()[2]
        return top 





better1 = Bet("Sebastian", 200, 1,2,2)
better2 = Bet("Seba", 200, 1,2,2)

print(Bet.getTopThree())