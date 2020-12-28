from flask import Flask, session, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'sincos'


@app.route("/index", methods=["POST", "GET"])
def index():
    session['msg'] = 'sincos'
    flash('Welcome', category='f1')
    flash('Welcome', category='f2')
    return "index"


@app.route("/test", methods=["POST", "GET"])
def test():
    '''KeyError: 'msg'
    msg = session.pop('msg')'''
    msg = get_flashed_messages(category_filter=['f1'])
    print(msg)
    return "test"


# flash闪现，如果只执行一次或次数少就使用，其内部原理也算是session
if __name__ == '__main__':
    app.run(debug=True)
