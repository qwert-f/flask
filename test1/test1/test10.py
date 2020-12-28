from flask import Flask

app = Flask(__name__)

app.config["SERVER_NAME"] = 'wsda.com:5000'

# 实现子域名 xxx.wsda.com


# 动态子域名
@app.route("/test", subdomain="<admit>")
def static_domain(admit):
    print(admit)
    return admit+".domains"

# 静态子域名
# @app.route("/", subdomain="admit")
# def static_domain():
#     return "static domain"


if __name__ == '__main__':
    app.run(debug=True)
