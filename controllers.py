import sqlite3

def insert_password(username, password,hashpassword, strength):
    conn = sqlite3.connect('db/password.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, userpassword, hashpassword, strength) VALUES (?, ?, ?, ?)
    ''', (username, password, hashpassword, strength))
    conn.commit()
    conn.close()