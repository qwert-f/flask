# First Flask web test
![项目logo](https://sincos.ga/logo.jpg)

[麻省理工学院许可证 （MIT）](https://raw.githubusercontent.com/qwert-f/flask/main/LICENSE)
### 1.项目中用到的python有关的库

    PyMySQL==0.10.1
    redis==3.5.3
    Flask==1.1.2
    Flask_Session==0.3.2
    WTForms==2.3.3
    DBUtils==2.0
    email-validator==1.1.2
    sqlalchemy==1.3.20

项目在迁移过程中使用了python的pipreqs来解决对项目中依赖的库的的快速安装
对于pipreqs的使用

可参见：
[pipreqs解决项目依赖](https://sincos.ga/reqs.html)

### 2.项目目录结构

    components  根目录
      ---components 根目录同名目录
        --templates 模板目录
          -home.html  主页
          -login.html 登录页
          -register.html  注册页
        --utils 公共文件目录
          -pools.py 数据库连接池
          -sql.py 关联数据库(原生SQL)
        --views 视图目录
          -account.py 用户账户有关的(注册，登录)
          -home 主页的逻辑操作
        --__init__.py 初始化
        --models.py SQLAlchemy操作数据库(基于ORM）
      ---setting.py 项目所有的设置
      ---manage.py  项目启动文件

### 3.项目用到的技术
**3.1:**
***redis***

在项目中主要用于存储原本在flask框架中存放在浏览器cookies中的sesssion
,并进行随机验证码的存储，以便可以快速完成验证，避免因采用数据库存储，访问时间长导致的速度慢 ***最近太忙没时间开发***

**3.2**
***js,canvas,css,html***

对于部分的页面跳转并未采用python中的，用户注册时的随机验证码，字符由js随机生成，并通过canvas绘制呈现，页面基础框架由html构成(表单部分由WTForms完成)，页面的样式由css进行美化(其中主页的两个轮播图，分别用css动画和js计时器完成)***目前轮播的还没开发***

**3.3**
***mysql***

用户的数据等均由mysql存储，对于mysql与python之间交互,由python的库PyMySQL和SQLAlchemy,数据库连接池采用DBUtils共享连接的方式完成，这样做的目的是为了避免对于数据频繁操作。

**3.4**
***email-validator***

用户注册时，邮箱的验证并像限定用户名和密码一样，采用正则表达式来实现对于邮箱格式的限定,而是直接使用emial-validator来完成

### 4.项目部署[1]
nginx+gunicorn+Flask
通过nginx代理，gunicorn用于将项目启动，而不是python XXX.py的方式运行

更多信息见开发网站
[DevWebsite](https://sincos.ga)

[1]:***注：部署并未成功实现通过域名访问，虽然做了域名解析等，可能的原因还在还在找，目前正在验证猜测的原因***
