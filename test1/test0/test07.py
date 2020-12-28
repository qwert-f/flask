from flask import Flask

app = Flask(__name__)

'''
常用路由系统
@app.route('/xxx/<username>')
           '/xxx/<int:post_id>'
           '/xxx/<float:post_id>'
           '/xxx/<path:path>'
           '/xxx/<methods=['POST', 'GET']>'
所有路由系统都是基于以下对应关系来处理
DEFAULT_CONVERTERS = {
    'default': 'UnicodeConverter'
    'string': 'UnicodeConverter'
    'any': 'AnyConverter'
    'path': 'PathConverter'
    'int': 'IntegetrConverter'
    'float': 'FloatConverter'
    'uuid': 'UUIDConverter'
}
'''


@app.route("/test07/<int:nid>", methods=["POST", "GET"])
def test07(nid):
    print(nid, type(nid))
    return "none"


if __name__ == '__main__':
    app.run()
