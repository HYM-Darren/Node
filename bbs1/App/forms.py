import re

from flask_wtf.file import FileAllowed

from ext import photos
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,FileField
from wtforms.validators import  Length,Email,EqualTo,DataRequired,ValidationError
from .model import User

class RegisterForm(FlaskForm):
    username = StringField('用户名:',validators=[DataRequired("用户名必须输入"),
                                              Length(min=3,max=20,message="用户名长度必须在3-20之间")])
    password = PasswordField("密码:",validators=[Length(6,12,message="密码长度必须在6~12位之间"),DataRequired()])
    confirm = PasswordField("密码确认:",validators=[DataRequired(),EqualTo('password',message="两次密码输入不一致")])
    email = StringField("邮箱:",validators=[Email(message="邮箱格式错误")])
    submit  = SubmitField("注册")
    # 自定义验证
    def validate_username(self,field):
        # 获取用户输入的值使用field.data
        print(field,field.data)
        res = User.query.filter(User.username==field.data).all()
        print(res)
        if res:
            raise ValidationError("用户名已经重复")

    def validate_password(self,field):
        if re.match(r'\d+$',field.data):
            raise ValidationError("密码不能是纯数字")

# 文件上传表单
class UploadForm(FlaskForm):
    photo = FileField('头像',validators=[DataRequired(),FileAllowed(photos,message="只能上传图片")])
    submit = SubmitField()