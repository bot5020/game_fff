import sqlite3

connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
              (Title TEXT, Director TEXT, Year INT)''')

moreShows = [('Money Heist', 'Alex Rodrigo', 2017),
             ('Dark', 'Baran bo Odar', 2017),
             ('1992 Scam', 'Hansal Mehta', 2020)]

cursor.executemany("INSERT INTO Shows VALUES (?, ?, ?)", moreShows)
records = cursor.execute("SELECT * FROM Shows")

print(cursor.fetchall())

connection.commit()
connection.close()