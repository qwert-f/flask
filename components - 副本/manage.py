from components import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
# 运行时请先输入login路由,用户名Emma,密码1234，然后成功跳转index路由后，则可以跳转test路由，否则报错
