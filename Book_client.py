import sqlite3
con = sqlite3.connect('Book.db')

c = con.cursor()

c.execute("SELECT signature FROM Books")

row = c.fetchone()
while row:
    print("이름:",c.fetchmany(size=1))
    row = c.fetchone()

c.close()
con.close()