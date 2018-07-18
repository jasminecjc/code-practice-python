# -*- coding: utf-8 -*-
import sys
from sqlalchemy import create_engine
import pandas as pd

host = '127.0.0.1'
port = 3306
db = 'test'
user = 'root'
password = 'root'

engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' +
                           "@%s/%s?charset=utf8") % (user, password, host, db))

try:
    df = pd.read_csv(r'test.csv', encoding='utf-8')
    df['id'] = range(1, len(df) + 1)
    print(df)
    df.to_sql('test', con=engine, if_exists='append', index=False)
except Exception as e:
    print(e.message)
