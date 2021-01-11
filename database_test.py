import sqlite3
conn = sqlite3.connect('stock-data.db')
c= conn.cursor()
c.execute(''' CREATE TABLE SZ000002
          (ID       INT PRIMARY KEY  NOT NULL,
           TIME         TEXT     NOT NULL,
           CODE         TEXT      NOT NULL,
           HIGH         REAL,
           LOW           REAL,
           CLOSE         REAL,
           OPEN           REAL,
           DESCRIPTION CHAR(50)); ''')
conn.commit()
c.execute("PRAGMA table_info(SZ000002)")
print(c.fetchall())
