import bet
import os 


if os.path.isfile("betters.db") != True:
    print("No database, creates.....")
    conn = bet.Bet.create_connection("betters.db")
    with conn:
        bet.Bet.create_table(conn,"""CREATE TABLE IF NOT EXISTS betters (
            id integer PRIMARY KEY,
            name text NOT NULL,
            bet integer,
            p1 text,
            p2 text,
            p3 text
        );""") 
else:
    print("Database exist!")





def addPlayer(name, theBet, p1, p2, p3):
    

    with conn:
        better = bet.Bet(name, theBet, p1, p2, p3)
        objekt = (better.name, better.bet, better.posOne, better.posTwo, better.posThree)
        bet.Bet.save_bet(conn, objekt)

        del better


""" def getPlayers():
    players = pickle.load(open("bet_data.pk1", 'rb'))
    return players
 """


#better1.checkBets()
addPlayer("Filip", 200, "HAM", "BOT", "VET")
