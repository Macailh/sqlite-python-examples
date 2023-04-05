import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Juan"),
        (3, "Pedro"),
    ]
    cursor.execute("INSERT INTO usuarios values(?,?)", usuarios)
