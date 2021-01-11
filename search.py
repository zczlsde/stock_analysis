import sqlite3
conn = sqlite3.connect('stock-data.db')
c= conn.cursor()
c.execute("SELECT id, time, code, description from SZ000002 where HIGH<10.15 and HIGH >10.12")
for row in c:
    print("ID = {}; TIME = {};CODE = {}; DESCRIPTION = {};".format (row[0],row[1],row[2],row[3]))
