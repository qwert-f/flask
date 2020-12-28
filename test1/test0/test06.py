from flask import Flask, url_for

app = Flask(__name__)


@app.route("/test", methods=["POST", "GET"], endpoint='N1')
def test():
    v1 = url_for('N1')
    v2 = url_for('N2')
    v3 = url_for('te')
    print(v2, v3, v1)
    return "test"


@app.route("/tes", methods=["POST", "GET"], endpoint='N2')
def tes():
    return "tes"


@app.route("/te", methods=["POST", "GET"])  # 反向url默认是函数名
def te():
    return "te"


if __name__ == '__main__':
    app.run()
