import sqlite3
conn = sqlite3.connect('stock-data.db')
c= conn.cursor()
c.execute("INSERT INTO SZ000002(ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
             VALUES(1,'2019-1-1', 000002, 10.12, 10.12, 10.12, 10.12, 'Buy Sinal'  )")
c.execute("INSERT INTO SZ000002(ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
             VALUES(2,'2019-1-2', 000002, 10.13, 10.13, 10.13, 10.13, 'Sell Sinal'  )")
c.execute("INSERT INTO SZ000002(ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
             VALUES(3,'2019-1-3', 000002, 10.14, 10.14, 10.14,10.14, 'Buy Sinal'  )")
c.execute("INSERT INTO SZ000002(ID,TIME,CODE,HIGH,LOW,CLOSE,OPEN,DESCRIPTION) \
             VALUES(4,'2019-1-4', 000002, 10.15, 10.15, 10.15, 10.15, 'Sell Sinal'  )")
conn.commit()
c.execute("select * from SZ000002")
print(c.fetchall())