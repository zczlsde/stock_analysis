import sqlite3
import tushare as ts
import pandas as pd
conn = sqlite3.connect('stock-data.db')
token = 'ff4c2656499bb1540627db337f965353cf98509d6cd4b479ee509bb1'
pro = ts.pro_api(token)
df_gldq = pro.daily(ts_code  = '000651.SZ', start_date = '20190101', end_date='20190201')
#print(df_gldq.head())
df_gldq.to_sql(name='STOCK000651',
               con = conn,
               index =False,
               if_exists='replace')
sql_gldq = pd.read_sql_query("select * from 'STOCK000651';", conn)
print(sql_gldq.head())