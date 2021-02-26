from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine, ForeignKey, UniqueConstraint
import datetime

from sqlalchemy.orm import relationship

Base = declarative_base()


class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=True)


class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(48), default="eating")

# 创建多对多关系的表


class Student2Hobby(Base):
    __tablename__ = 'student2hobby'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    hobby_id = Column(Integer, ForeignKey("hobby.id"))
    __table_args__ = (
        # 联合唯一索引
        UniqueConstraint('student_id', 'hobby_id',
                         name='uix_student_id_hobby_id'),
        # 普通联合索引
        # Index('ix_id_name', 'name', 'extra'),
    )


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, index=True)
    pwd = Column(String(64), nullable=False)
    ctime = Column(DateTime, default=datetime.datetime.now)
    flask_id = Column(Integer, ForeignKey("classes.id"))
    # 表关系,一张表可以多种关系，进行关联查询
    cls = relationship('Classes', backref='stus')


def init_db():
    engine = create_engine("mysql+pymysql://root:sql1@127.0.0.1:3306/dailys")
    Base.metadata.create_all(engine)


def drop_db():
    engine = create_engine("mysql+pymysql://root:sql1@127.0.0.1:3306/dailys")
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    # drop_db()
    init_db()
