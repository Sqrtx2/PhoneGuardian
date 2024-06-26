import sqlite3
from Server.ServerLogic.Identity import Identity
from LookUp import Database



def search_location(pnumber):
    db_path = "LookUp/PhoneNumber.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    search_key = pnumber[0:2]
    cursor.execute( "SELECT area FROM location WHERE key = ?", (search_key,))

    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        return None

def search_flagged(pnumber):
    db_path = "LookUp/PhoneNumber.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    search_key = pnumber
    cursor.execute( "SELECT pnumber FROM flagged WHERE pnumber = ?", (search_key,))

    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        return None
    
def search_provider(pnumber):
    db_path = "LookUp/PhoneNumber.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    search_key = pnumber[0:5]
    print(search_key)
    cursor.execute( "SELECT provider FROM providers WHERE key = ?", (search_key,))

    result = cursor.fetchone()

    if result:
        return result[0]
    elif pnumber[2:4] == "80":
        # Bezeg has a unique identifier which is why it is not in the database
        return "Bezeq"
    else:
        return None

def search(pnumber):
    caller_identity = Identity(search_location(pnumber), search_flagged(pnumber), search_provider(pnumber))
    return str(caller_identity)