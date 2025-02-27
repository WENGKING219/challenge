import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
cursor.execute('INSERT INTO users (username, password) VALUES ("admin", "secret")')
conn.commit()
conn.close()