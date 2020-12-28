from flask import Flask, render_template, Markup

app = Flask(__name__)


def input(value):
    # Markup()确保安全
    return Markup("<input value='%s'?>" % value)


@app.template_global()  # 全局定义，每个模板都可以使用
def globals(value):
    return value


@app.template_filter()
def filters(a, b, c):
    return a+b+c


@app.route("/test", methods=["POST", "GET"])
def test():
    content = {
        'a1': 123,
        'a2': [12, 23, 34],
        'a3': {'name': 'sin', 'age': 12},
        'a4': lambda x: x+1,
        'a5': input,
        'global': globals
        # 当前模板可调用
    }
    return render_template('test14.html', **content)


@app.route('/test14_1')
def test14_1():
    content = {
        'globals': globals,
        'filter': filters,
    }
    return render_template('test14_1.html', **content)


if __name__ == '__main__':
    app.run(debug=True)
