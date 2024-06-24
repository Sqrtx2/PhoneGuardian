import sqlite3
import os


db_path = "LookUp/PhoneNumber.db"

connection = sqlite3.connect(db_path)

cursor = connection.cursor()

pnumber = input("enter a phone number ")

try:
    cursor.execute("""
                CREATE TABLE location (
                key VARCHAR(255) PRIMARY KEY,
                    area TEXT
                )
                """)
    
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

search_key = pnumber[0:2]
cursor.execute( "SELECT area FROM location WHERE key = ?", (search_key,))

result = cursor.fetchone()

if result:
    print(result[0])
else:
    print("No matches found")

connection.commit()

connection.close()