
from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

# werkzeug提供关于路径解析设置的工具，BaseConverter转换器父类

# 创建flask应用对象
# __name__表示当前的模块名字
# 模块名，flask以整个模块所在的目录为总目录，默认整个目录中的static为静态目录
# templates为模板目录
app = Flask(__name__)


# 转换器
# @app.route("/goods/<int:goods_id>")   转换器类型为int
@app.route("/goods/<goods_id>")  # 不加转换器类型，默认是普通字符串规则（除了/的字符）
def goods_detail(goods_id):
    """
    定义的视图函数
    :return:
    """
    return "goods detail page %s" % goods_id

# 1.定义自己的转换器


class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super().__init__(url_map)
        self.regex = r'1[34578]\d{9}'


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

    # def to_python(self, value):
    #     print("to_python方法被调用")
    #     # return "abc"
    #
    # def to_url(self, value):
    #     pass


# 2. 将自定义的转换器添加到flask的应用中,只把类存进去，没有创建对象
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] = MobileConverter


@app.route("/send/<re('1[3-8]\\d{9}'):mobile_num>")
# @app.route("/send/<mobile:mobile_num>")
def send_sms(mobile_num):
    return "send sms to %s " % mobile_num


@app.route("/index")
def index():
    url = url_for("send_sms", mobile_num="18222222222")
    # 路径/send/18922222222
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中路由信息
    print(app.url_map)
    app.run(debug=True)
