from flask import Flask

app = Flask(__name__)
app.config.from_object("setting.DEV")

'''
1.执行decorator=app.route("/test05",methods=["POST", "GET"])
2.@decorator
    -- decorator(index)
'''

# 路由方式一


@app.route("/test05", methods=["POST", "GET"])
def test05():
    return "none"
# 路由方式二


def order():
    return 'order'


app.add_url_rule("/order", view_func=order)

if __name__ == '__main__':
    app.run()
