import sqlite3
con = sqlite3.connect('Book.db')

con.execute("SELECT * FROM Books")

print(con)

con.close()