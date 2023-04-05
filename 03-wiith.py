import sqlite3

with sqlite3.connect('sqlite/app.db') as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY, nombre VARCHAR(50))
        """)
