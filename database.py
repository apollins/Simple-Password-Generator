import sqlite3

connection = sqlite3.connect('db/password.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
userpassword TEXT NOT NULL,
hashpassword TEXT NOT NULL,
strength TEXT NOT NULL 
)
''')

connection.commit()
connection.close()