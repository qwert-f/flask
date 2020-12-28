from flask import Flask

app = Flask(__name__)

'''
before_request = {before, befores}
'''


@app.before_request
def before():
    print('before')


@app.before_request
def befores():
    print('befores')


'''
after_request = {after, afters}
{afters,after} = eversed(after_request)
'''


@app.after_request
def after(request):
    print('after')
    return request


@app.after_request
def afters(request):
    print('afters')
    return request


@app.route("/index", methods=["POST", "GET"])
def index():
    return "index"


@app.route("/test", methods=["POST", "GET"])
def test():
    return "test"


if __name__ == '__main__':
    app.run(debug=True)
