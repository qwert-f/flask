from redis import Redis
# ImportError: cannot import name 'Redis' from partially initialized module 'r
# 报错原因是文件名与系统的文件名重名，导致程序无法识别，从而判定为循环导包
conn = Redis(host='127.0.0.1', port='6379',  password='redis1')
v = conn.keys()
print(v)
