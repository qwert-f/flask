import pymysql
from flask import current_app


class SQLHelper(object):
    @staticmethod  # 静态字段
    def openSQL():
        # conn = pymysql.connect(host='127.0.0.1', port=3306,
        #                        user='root', password='sql1', db='daily')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        POOL = current_app.config['PYMYSQL_POOL']
        conn = POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    @staticmethod
    def closeSQL(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def fetch_one(sql, args):
        # conn = pymysql.connect(host='127.0.0.1', port='3306',
        #                        user='root', password='sql1', db='daily')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn, cursor = SQLHelper.openSQL()

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
    def fetch_all(cls, sql, args):
        # conn = pymysql.connect(host='127.0.0.1', port='3306',
        #                        user='root', password='sql1', db='daily')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn, cursor = cls.openSQL()

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
