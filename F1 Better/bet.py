# Add bet
# Follow Race
# Get current leader during race
# Get sum of Bet
# Create a bot

import requests
import json
import sqlite3
from sqlite3 import Error

class Bet:

    pot = 0


    def __init__(self, name, bet, posOne, posTwo, posThree):
        self. name = name
        self.bet = bet
        self.posOne = posOne
        self.posTwo = posTwo
        self.posThree = posThree

    def checkBets(self):
        winners = self.getDriverCodePosition()
        if self.posOne == winners[0] and self.posTwo == winners[1] and self.posThree == winners[2]:
            print("Winner of pot")
        else:
            print("Better luck next race")
            print("Top Three is 1: %s 2: %s 3: %s"%(winners[0],winners[1],winners[2]))
            print("Your Bet was 1: %s 2: %s 3: %s"%(self.posOne, self.posTwo, self.posThree))


   
    
    


    @classmethod
    def get_race_data(self, endpoint):
        """Gets JSON data from API"""
        BASE_URL = 'http://ergast.com/api/f1' 
        url = "%s/%s"%(BASE_URL, endpoint)
        r = requests.get(url)
        if r.status_code == 200:           
            json_data = json.loads(r.text)
            return json_data        
        else:
            print("Error " + str(r.status_code))
            return False

    @classmethod
    def get_race_results(self):
        """Gives back a list with the complete table"""

        final = []

            
        json_data = self.get_race_data("current/last/results.json")
        for i in json_data["MRData"]["RaceTable"]["Races"][0]["Results"]:
            final.append(i["position"] + ": " + i["Driver"]["givenName"] + " " + i["Driver"]["familyName"] + " Team: " + i["Constructor"]["name"])

        return final

    @classmethod
    def getTopThree(self):
        top = Bet.get_race_results()[0] + "\n", Bet.get_race_results()[1] + "\n", Bet.get_race_results()[2]
        return top 

    @classmethod
    def getDriverCodePosition(self):
        topThree = []
        json_data = self.get_race_data("current/last/results.json")
        topThree.append(json_data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["code"])
        topThree.append(json_data["MRData"]["RaceTable"]["Races"][0]["Results"][1]["Driver"]["code"])
        topThree.append(json_data["MRData"]["RaceTable"]["Races"][0]["Results"][2]["Driver"]["code"])
        return topThree
    @classmethod
    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """

        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
    
        return conn
    @classmethod
    def create_table(self, conn, sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        
        try:
            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    @classmethod
    def save_bet(self, conn, better):
        """
        Create a new project into the projects table
        :param conn:
        :param better:
        :return: project id
        """
        sql = ''' INSERT INTO betters(name,bet,p1,p2,p3)
                VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, better)
        return cur.lastrowid
    @classmethod
    def select_all(self,conn, table, player):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        output = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM %s WHERE name = 'Filip'"%(table))
    
        rows = cur.fetchall()
    
        for row in rows:
            print(row)
            return output.append(row)
    @classmethod
    def select_pot(self, conn):
        """
        Get sum of bets
        
        :return: um
        """
     
        cur = conn.cursor()
        cur.execute("SELECT SUM(bet) FROM betters")
    
        pot = cur.fetchall()
    
        return pot[0][0]
    



