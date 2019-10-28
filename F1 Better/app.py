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
    conn = bet.Bet.create_connection("betters.db")
    print("Database exist!")



def Main():
    print("""Choose
            1. Add player
            2. Show Players
            3. Show specific player
            """)
    choice = input("Choose a menuitem: ")
    if choice == "1":
        addPlayer()

def addPlayer():
    name = input("Whats your name: ")
    bet = input("How much do you want to bet 1-500 kr")
    print("Use the driver code for the top three example HAM for Hamilton")
    p1 = input("Who comes first?")
    p2 = input("Who comes second?")
    p3 = input("Who comes third?")
    savePlayer(name, bet, p1,p2,p3)
def savePlayer(name, theBet, p1, p2, p3):
    

    with conn:
        better = bet.Bet(name, theBet, p1, p2, p3)
        objekt = (better.name, better.bet, better.posOne, better.posTwo, better.posThree)
        bet.Bet.save_bet(conn, objekt)

        del better


def getPlayers():
    #conn = bet.Bet.create_connection("betters.db")
    with conn:
        getAll = bet.Bet.select_all(conn, "betters", "*")
        return getAll

def getPlayer(name):
    #conn = bet.Bet.create_connection("betters.db")
    with conn:
        getAll = bet.Bet.select_all(conn, "betters", name)
        return getAll



#better1.checkBets()
#addPlayer("Filip", 200, "HAM", "BOT", "VET")
print(getPlayer("*"))

if __name__=="__main__":
    Main()