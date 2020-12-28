import pymysql
# from flask import current_app  # 方法1
from settings import Config


class SQLHelper(object):
    @staticmethod  # 静态字段
    def openSQL(cursor):
        # from .pools import POOL  # 方法2
        # conn = pymysql.connect(host='127.0.0.1', port=3306,
        #                        user='root', password='sql1', db='daily')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # POOL = current_app.config['PYMYSQL_POOL']     # 方法1.2
        POOL = Config.PYMYSQL_POOL
        conn = POOL.connection()
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor = conn.cursor(cursor=cursor)
        return conn, cursor

    @staticmethod
    def closeSQL(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def fetch_one(sql, args, cursor=pymysql.cursors.DictCursor):
        # conn = pymysql.connect(host='127.0.0.1', port='3306',
        #                        user='root', password='sql1', db='daily')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn, cursor = SQLHelper.openSQL(cursor)

        # cursor.execute(
        #     "select id,name from users where name=%s and pwd=%s",
        # [user, pwd, ])

        cursor.execute(sql, args)
        obj = cursor.fetchone()

        SQLHelper.closeSQL(conn, cursor)
        # conn.commit()
        # cursor.close()
        # conn.close()
        return obj

    @classmethod
    def fetch_all(cls, sql, args, cursor=pymysql.cursors.DictCursor):
        # conn = pymysql.connect(host='127.0.0.1', port='3306',
        #                        user='root', password='sql1', db='daily')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn, cursor = cls.openSQL(cursor)

        # cursor.execute(
        #     "select id,name from users where name=%s and pwd=%s",
        # [user, pwd, ])

        cursor.execute(sql, args)
        obj = cursor.fetchall()

        cls.closeSQL(conn, cursor)
        # conn.commit()
        # cursor.close()
        # conn.close()
        return obj
