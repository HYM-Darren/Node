from ext import db
from werkzeug.security import generate_password_hash
class DBBase:
    # 保存记录
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    #   保存多条记录
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()
    #  删除自己
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()

class Category(db.Model,DBBase):
    id = db.Column(db.Integer,primary_key=True)
    classname = db.Column(db.String(60),nullable=False)
    parentid = db.Column(db.Integer,nullable=False)
    replycount = db.Column(db.Integer,nullable=False)
    compere = db.Column(db.String(10))
    description  = db.Column(db.String(1000))
    orderby = db.Column(db.Integer,nullable=False)
    lastpost = db.Column(db.String(600))
    namestyle = db.Column(db.String(10))
    ispass = db.Column(db.SmallInteger,nullable=False)
    classpic = db.Column(db.String(20))
    themecount = db.Column(db.Integer,nullable=False)
    __tablename__ = 'bbs_category'

class User(db.Model,DBBase):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(16),nullable=False)
    password = db.Column(db.String(32),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    udertype = db.Column(db.Integer,nullable=False)
    regtime = db.Column(db.Integer,nullable=False)
    lasttime = db.Column(db.Integer,nullable=False)
    regip = db.Column(db.Integer,nullable=False)
    picture = db.Column(db.String(255),nullable=False,default='public/images/avatar_blank.gif')
    grade = db.Column(db.Integer,default=0)
    problem = db.Column(db.String(200))
    result = db.Column(db.String(200))
    realname = db.Column(db.String(50))
    sex = db.Column(db.Integer,default=2)
    birthday = db.Column(db.String(20))
    place = db.Column(db.String(50))
    qq = db.Column(db.String(13))
    autograph = db.Column(db.String(500))
    allowlogin = db.Column(db.Integer,nullable=False)
    __tablename__ = 'bbs_user'
    # @property
    # def password(self):
    #     return self.__password
    # @password.setter
    # def password(self,value):
    #     return generate_password_hash(value)
    def validate_password(self,password):
        return check_password_hash(self.__password,password)

class Details(db.Model,DBBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first = db.Column(db.Integer,nullable=False,default=0)
    tid = db.Column(db.Integer,nullable=False)
    authorid = db.Column(db.Integer,nullable=False)
    title = db.Column(db.String(600),nullable=False)
    content = db.Column(db.String(600),nullable=False)
    addtime = db.Column(db.Integer,nullable=False)
    addip = db.Column(db.Integer,nullable=False)
    classid = db.Column(db.Integer,nullable=False)
    replycount = db.Column(db.Integer,nullable=False,default=0)
    hits = db.Column(db.Integer, nullable=False, default=0)
    istop = db.Column(db.Integer, nullable=False, default=0)
    elite = db.Column(db.Integer, nullable=False, default=0)
    ishot = db.Column(db.Integer, nullable=False, default=0)
    rate = db.Column(db.Integer, nullable=False, default=0)
    attachment = db.Column(db.Integer)
    isdel = db.Column(db.Integer, nullable=False)
    style = db.Column(db.String(10))
    isdisplay = db.Column(db.Integer, nullable=False)
    __tablename__ = 'bbs_details'


class closeip(db.Model, DBBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    overtime = db.Column(db.Integer)
    __tablename__ = 'bbs_closeip'


class link(db.Model, DBBase):
    lid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    displayorder = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    logo = db.Column(db.String(255))
    addtime = db.Column(db.Integer, nullable=False)
    __tablename__ = 'bbs_link'


class order(db.Model, DBBase):
    oid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, nullable=False)
    tid = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    ispay = db.Column(db.Integer, nullable=False, default=0)
    __tablename__ = 'bbs_order'