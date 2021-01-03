from sqlalchemy import create_engine


class sql():
    engine = create_engine('mysql+pymysql://root:sql1@127.0.0.1:3306/daily')
    cur = engine.execute('select name from users')


# result = sql.cur.fetchall()
# print(result)