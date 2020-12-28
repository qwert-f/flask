from flask import Flask

app = Flask(__name__)

'''
前端重定向
1.meta:content
2.js
'''


@app.route("/test", methods=["POST", "GET"], redirect_to='/new')    # 重定向到new
def test():
    return "test"


@app.route("/new", methods=["POST", "GET"])
def new():
    return "new"


if __name__ == '__main__':
    app.run(debug=True)
