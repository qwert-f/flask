from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# class sql():
#     engine = create_engine('mysql+pymysql://root:sql1@127.0.0.1:3306/daily')
#     # engine = create_engine('mysql+pymysql://root:aws@ubuntu@127.0.0.1:3306/flask')
#     cur = engine.execute('select name from users')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=True)
    pwd = Column(String(64), unique=True)


def init_db():
    engine = create_engine("mysql+pymysql://root:sql1@127.0.0.1:3306/daily")
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    # drop_db()
    init_db()

# result = sql.cur.fetchall()
# print(result)
