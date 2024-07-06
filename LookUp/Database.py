import sqlite3
import os


db_path = "LookUp/PhoneNumber.db"

connection = sqlite3.connect(db_path)

cursor = connection.cursor()


try:
    # Caller location table
    cursor.execute("""
                CREATE TABLE location (
                key VARCHAR(255) PRIMARY KEY,
                    area TEXT
                )
                """)
except Exception as ex:
    print(ex)

try:
    cursor.execute("""
                    INSERT INTO location VALUES
                    ('02', 'Jerusalem'),
                    ('03', 'Tel Aviv-Yafo and center'),
                    ('04', 'Haifa and north'),
                    ('08', 'South and lowlands'),
                    ('09', 'Hasharon')
                    """)
except Exception as ex:
    print(ex)

try:
    # Flagged by users caller table
    cursor.execute("""
                   CREATE TABLE flagged (
                   pnumber VARCHAR(255) PRIMARY KEY
                   )
                   """)
except Exception as ex:
    print(ex)
try:
    cursor.execute("""
                   INSERT INTO flagged VALUES
                   ('0543462329')
                   """)
except Exception as ex:
    print(ex)

try:
    # Caller provider table
    cursor.execute("""
                CREATE TABLE providers (
                key VARCHAR(255) PRIMARY KEY,
                    provider TEXT
                )
                """)
except Exception as ex:
    print(ex)

try:
    cursor.execute("""
                    INSERT INTO providers VALUES
                    ('050', 'Pelephone'),
                    ('052', 'Cellcom'),
                    ('053', 'Hot mobile'),
                    ('057', 'Hot mobile'),
                    ('054', 'Partner'),
                    ('058', 'Golan telecom')
                    """)
except Exception as ex:
    print(ex)



''' 
pnumber = input("enter a phone number ")

# location
 search_key = pnumber[0:2]
 cursor.execute( "SELECT area FROM location WHERE key = ?", (search_key,))

 result = cursor.fetchone()

if result:
    print(result[0])
else:
    print("No location matches have been found")

# flagged
search_key = pnumber
cursor.execute('SELECT pnumber FROM flagged WHERE pnumber = ?', (search_key,))

result = cursor.fetchone()
if result:
    print("The given phone number is flagged")
else:
    print("The given phone number is not flagged") '''

connection.commit()

connection.close()