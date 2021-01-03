from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# from uuid import uuid4
from ..utils.sql import SQLHelper
from wtforms import Form
# from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

account = Blueprint('account', __name__)


class LoginForm(Form):
    user = simple.StringField(
        # label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(
                max=18, message='用户名长度必须小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}

    )
    pwd = simple.PasswordField(
        # label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )


@account.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if not form.validate():
            return render_template('login.html', form=form)
        print("submit right,value is:", form.data)
    # user = request.form.get('user')
    # pwd = request.form.get('pwd')
    # 连接数据库--->查询--->关闭数据库
    obj = SQLHelper.fetch_one(
        # "select id,name from users where name=%s and pwd=%s", [user, pwd, ])
        "select id,name from users where name=%(user)s and pwd=%(pwd)s", form.data)
    if obj:
        # if user == 'ama' and pwd == '1234':
        # uid = str(uuid4())
        session.permanent = True    # redis默认设置了为true
        # session['user_info'] = {'id': uid, 'name': user}
        session['user_info'] = {'id': obj['id'], 'name': obj['name']}
        return redirect('/')
    else:
        return render_template('login.html', msg='用户名或密码错误！', form=form)


class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            # validators.Length(min=8, message='用户名长度必须小于%(min)d'),
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='Emma'
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Regexp(regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

            ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    # gender = core.RadioField(
    #     label='性别',
    #     choices=(
    #         (1, '男'),
    #         (2, '女'),
    #     ),
    #     coerce=int
    # )
    # city = core.SelectField(
    #     label='城市',
    #     # choices=(
    #     #     ('bj', '北京'),
    #     #     ('sh', '上海'),
    #     # )
    #     choices=SQLHelper.fetch_all('select id, name from city', {}, None),
    # )

    # hobby = core.SelectMultipleField(
    #     label='爱好',
    #     choices=(
    #         ('1', '篮球'),
    #         ('2', '足球'),
    #     ),
    #     # choices中序号是数字是需要下面的，但是但序号是字符是不需要。原因是格式
    #     # coerce=int
    # )

    # favor = core.SelectMultipleField(
    #     label='喜好',
    #     choices=(
    #         (1, '篮球'),
    #         (2, '足球'),
    #     ),
    #     widget=widgets.ListWidget(prefix_label=False),
    #     option_widget=widgets.CheckboxInput(),
    #     coerce=int,
    #     default=[1, 2]
    # )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))
        # 更新同步数据库中的改变
        # self.city.choices = SQLHelper.fetch_all(
        #     'select id, name from city', {}, None)

    # 钩子函数
    # def validate_pwd_confirm(self, field):
    # def validate_name(self, field):
    #     """
    #     自定义pwd_confirm字段规则，例：与pwd字段是否一致
    #     :param field:
    #     :return:
    #     """
    #     # 最开始初始化时，self.data中已经有所有的值
    #     # print(field.data)   # 当前name传过来的值
    #     # print(self.data)    # 当前传过来的所有得知：name,gender...
    #     obj = SQLHelper.fetch_one(
    #         'select id from users where name=%s', [field.data, ])
    #     if obj:
    #         raise validators.ValidationError("用户名已经存在")
        # if field.data != self.data['pwd']:
        #     # raise validators.ValidationError("密码不一致") # 继续后续验证
        #     raise validators.StopValidation("密码不一致")  # 不再继续后续验证


@account.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form=form)
    form = RegisterForm(formdata=request.form)
    if form.validate():
        # print(form.data)
        # 注册完成跳转登录页面
        return redirect(url_for('account.login'))
    else:
        # print(form.errors)
        # return redirect(url_for('account.register'), msgs="用户名已存在")
        # form = RegisterForm()
        return render_template('register.html', form=form)
