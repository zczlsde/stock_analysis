import sqlite3
conn = sqlite3.connect('stock-data.db')
c= conn.cursor()
c.execute("UPDATE SZ000002 set DESCRIPTION = 'NONE' WHERE ID = 1")
conn.commit()
c.execute("select * from SZ000002")
print(c.fetchall())
