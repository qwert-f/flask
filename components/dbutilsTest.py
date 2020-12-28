'''
import pymysql
from DBUtils.PersistentDB import PersistentDB

POOL = PersistentDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    setsession=[],
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    # 如：0 = None = never, 1 = default = whenever it is requested,
    # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,
    # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。
    # 如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，
    # 因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8'
)


def func():
    conn = POOL.connection(shareable=False)
    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    cursor.close()
    conn.close()


func()
'''
# import time
import pymysql
# import threading
from dbutils.pooled_db import PooledDB
# ModuleNotFoundError: No module named 'DBUtils'报错的原因是版本是2.0而下面的写法是1.3的写法
# from DBUtils.PooledDB import PooledDB, SharedDBConnection
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。
    # PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，
    # 所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。

    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。
    # 如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never,
    # 1 = default = whenever it is requested, 2 = when a cursor is created,
    # 4 = when a query is executed, 7 = always
    host='127.0.0.1',
    port=3306,
    user='root',
    password='sql1',
    database='daily',
    charset='utf8'
)


def func():
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
    conn = POOL.connection()

    # print(th, '链接被拿走了', conn1._con)
    # print(th, '池子里目前有', pool._idle_cache, '\r\n')

    cursor = conn.cursor()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 数据字典形式
    cursor.execute('select * from users')
    result = cursor.fetchall()
    conn.close()
    return result


ret = func()
print(ret)
