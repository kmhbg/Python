# Add bet
# Follow Race
# Get current leader during race
# Get sum of Bet
# Create a bot

import requests
import json
class Bet:

    pot = 0


    def __init__(self, name, bet, posOne, posTwo, posThree):
        self. name = name
        self.bet = bet
        self.posOne = posOne
        self.posTwo = posTwo
        self.posThree = posThree

    def checkBets(self):
        pass


   
    
    


    @classmethod
    def get_race_data(self, endpoint):
        """Gets JSON data from API"""
        BASE_URL = 'http://ergast.com/api/f1' 
        url = "%s/%s"%(BASE_URL, endpoint)
        r = requests.get(url)
        final = []
        if r.status_code == 200:           
            json_data = json.loads(r.text)
            return json_data        
        else:
            print("Error " + str(r.status_code))
            return False

    @classmethod
    def get_race_results(self):
        """Gives back a list with the complete table"""
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

    @classmethod
    def getResults(self):
        pass



Bet.get_race_data("current/last/results.json")