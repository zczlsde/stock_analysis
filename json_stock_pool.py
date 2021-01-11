import json
import tushare as ts

token = 'ff4c2656499bb1540627db337f965353cf98509d6cd4b479ee509bb1'
pro = ts.pro_api(token)
df = pro.stock_basic(exchange='', list_status='L')
#print(df)
codes = df.ts_code.values
names = df.name.values
stock = dict(zip(names,codes))
index = {'上证综指':'sh.000001',
        '深证指数':'sz.399001',
        '沪深300':'sz.000300',
        '创业板指':'sz.399006',
        '上证50':'sh.000016',
        '中证500':'sh.000905',
        '中小板指':'sz.399005',
        '上证180':'sh.000010'}
stock_index = dict([('指数',index),('股票',stock)])
with open('stock_pool.json','w',encoding='utf-8') as f:
    json.dump(stock_index,f,ensure_ascii=False,indent=4)

def json_to_str():
    with open("stock_pool.json",'r',encoding='utf-8') as load_f:
        stock_index = json.load(load_f)
    return stock_index

