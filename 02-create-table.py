import sqlite3

con = sqlite3.connect('sqlite/test.db')
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER PRIMARY KEY, nombre VARCHAR(50))
    """)
con.commit()
con.close()
