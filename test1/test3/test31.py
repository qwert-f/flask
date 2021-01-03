from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:sql1@127.0.0.1:3306/daily')
cur = engine.execute('select * from users')
result = cur.fetchall()
print(result)
