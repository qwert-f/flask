import test32
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("mysql+pymysql://root:sql1@127.0.0.1:3306/dailys")
database = sessionmaker(bind=engine)
session = database()

# 数据增删改查
# 单条增加
# obj = test32.Classes(name='信息2班')
# session.add(obj)
# session.commit()
# 多条增加
# objs = [
#     test32.Classes(name='信息1班'),
#     test32.Classes(name='数学1班'),
#     test32.Classes(name='数学2班')
# ]
# session.add_all(objs)
# session.commit()

# 查询
res = session.query(test32.Classes).all()
# for i in res:
#     print(i)
'''
查询结果
<test32.Classes object at 0x00000239A3FFDCD0>
<test32.Classes object at 0x00000239A3FFDC10>
<test32.Classes object at 0x00000239A3FFDBB0>
<test32.Classes object at 0x00000239A3FFD8E0>'''
# for i in res:
#     print(i.id, i.name)
'''
2 信息1班
1 信息2班
3 数学1班
4 数学2班'''
# select id,name form classes
result = session.query(test32.Classes.id, test32.Classes.name).all()
print(result)
for item in result:
    # print(item[0], item[1])
    print(item, type(item), item.name, item.id)
# select id,name as nm form Classes
result1 = session.query(
    test32.Classes.id, test32.Classes.name.label('nm')).all()
for i in result1:
    print(i.nm)
res1 = session.query(test32.Classes.name).filter_by(name='信息2班').all()
res2 = session.query(test32.Classes.name).filter_by(name='信息2班').first()
r6 = session.query(test32.Classes).filter(
    text("id<:value and name=:name")).params(value=224, name='fred').order_by(
    test32.Classes.id).all()
# 子查询
r7 = session.query(test32.Classes).from_statement(
    text("SELECT * FROM classes where name=:name")).params(name='ed')
r8 = session.query(test32.Classes).from_statement(
    text("SELECT * FROM classes where name=:name")).params(name='ed').all()
ret = session.query(test32.Classes).filter(test32.Classes.id.in_(
    session.query(test32.Classes.id).filter_by(name='eric'))).all()
# 关联子查询
# subqry = session.query(func.count(Server.id).label("sid")).
# filter(Server.id == Group.id).correlate(Group).as_scalar()
# result = session.query(Group.name, subqry)
print(res2, res1, r6, r7, r8, ret)

# 删除
# session.query(test32.Classes).filter(test32.Classes.id > 2).delete()
# session.commit()

# 修改
# 设置了unique无法进行下面的修改
# session.query(test32.Classes).filter(
#     test32.Classes.id > 2).update({"name": "数学院"})
# session.query(test32.Classes).filter(test32.Classes.id > 1).update(
#     {test32.Classes.name: test32.Classes.name+"数学院"},
#     synchronize_session=False)  # synchronize_session=False用于判断是字符串相加，还是算数运算加
# session.query(test32.Classes).filter(test32.Classes.id == 1).update(
#     {test32.Classes.id: test32.Classes.id+2},
#     synchronize_session="evaluate")
# session.commit()

session.close()
