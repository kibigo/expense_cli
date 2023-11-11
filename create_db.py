import sqlite3

conn = sqlite3.connect('expense.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS expense
(id INTEGER PRIMARY KEY,
date DATE,
description TEXT,
category TEXT,
price REAL)""")

conn.commit()
conn.close()