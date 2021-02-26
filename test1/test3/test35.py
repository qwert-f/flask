from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import test32

engine = create_engine("mysql+pymysql://root:sql1@127.0.0.1:3306/dailys")
database = sessionmaker(bind=engine)
session = database()

# 在学生表中插入数据
# obj = test32.Student(name='阿珍', pwd='1250s', flask_id=3)
# session.add(obj)

# 在学生表中找到阿珍
# obj=session.query(test32.Student).filter(test32.Student.name=='阿珍').first()
# print(obj)

# 找到所有学生，打印学生信息
# objs = session.query(test32.Student).all()
# for obj in objs:
#     cls_obj =session.query(test32.Classes).filter(test32.Classes.id==obj.flask_id).first()
#     print(obj.id, obj.name, obj.flask_id, cls_obj.name)

# objs = session.query(test32.Student).join(test32.Classes, isouter=True).all()
# print(objs)
# objs = session.query(test32.Student.id, test32.Student.name, test32.Classes.name).join(test32.Classes,
#                                                                                        isouter=True).all()
# print(objs)

# objs = session.query(test32.Student).all()
# for obj in objs:
#     print(obj.id, obj.name, obj.flask_id, obj.cls.name)

# 查找信息2班所有学生
sts = session.query(test32.Classes).filter(test32.Classes.name == '信息2班').first()
sts_obj = sts.stus
for item in sts_obj:
    print(item.id, item.name)

'''
更多可以看下面的博客
https://www.cnblogs.com/wupeiqi/articales/8259356.html'''
session.commit()
session.close()
