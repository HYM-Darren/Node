import re

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, Email, EqualTo, ValidationError, DataRequired, length
from .model import User
class Register(FlaskForm):
    username = StringField('用户名:',validators=[DataRequired("用户名必须输入"),length(min=3,max=2,message="用户名必须在3到20之间")])
    password = PasswordField('密码:',validators=[Length(6,12,message="密码必须在6~12之间"),DataRequired()])
    confirm = PasswordField('密码确认:',validators=[DataRequired(),EqualTo('password',message="两次密码输入不一致")])
    email = StringField('邮箱:',Email(message="邮箱格式不对"))

    def validate_username(self,field):
        res = User.query.filter(User.username==field.data).all()
        if res:
            raise ValidationError('ValidationError')

    def validate_password(self,field):
        if re.match(r'\d+$',field.data):
            raise ValidationError('密码不能纯数字')