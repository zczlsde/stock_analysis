import sqlite3
conn = sqlite3.connect('stock-data.db')
c= conn.cursor()
c.execute("DELETE from SZ000002 where ID=2;")
conn.commit()
c.execute("select * from SZ000002")
print(c.fetchall())
#c.execute("drop table SZ000002")
#conn.commit
conn.close()