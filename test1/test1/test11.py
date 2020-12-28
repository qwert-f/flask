from flask import Flask
import functools

app = Flask(__name__)


def wapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("before")
        return func(*args, **kwargs)
    return inner


@app.route("/test", methods=["POST", "GET"])
@wapper
def test():
    return "none"


@app.route("/tes", methods=["POST", "GET"])
@wapper
def tes():
    return "nones"


if __name__ == '__main__':
    app.run(debug=True)
