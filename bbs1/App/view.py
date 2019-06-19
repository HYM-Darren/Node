from flask import Blueprint, render_template, session,jsonify,current_app
from flask import Flask, make_response, request, redirect, url_for, session,Response
import time
import os
from datetime import timedelta

from sqlalchemy import func

from .VerfiCode import VerfiCode
from .model import *
from ext import db
bbs = Blueprint('bbs',__name__)

@bbs.route('/')
@bbs.route('/<int:cid>',methods=['GET','POST'])
def index(cid=0):
    # print(cid)
    # 大版块
    if cid == 0:
        bz = Category.query.filter(Category.parentid==cid).all()
    else:
        bz = Category.query.filter(Category.id==cid).all()
    # 所有大版块
    allBk = Category.query.filter(Category.parentid==0).all()
    # 小版块
    smallbz = Category.query.filter(Category.parentid!=0).all()
    dc = Details.query.get(1)
    # user = session['username']
    # datause = User.query.filter(User.password=='999',User.username=='999').all()
    user = User.query.get(1)
    themecount = Category.query.count()
    vipcount = User.query.count()
    # num = db.session.query(User).count()
    usernew = User.query.order_by(-User.id).all()[0]
    return render_template('index.html',**{
        'category':bz,
        'allBk':allBk,
        'smalls':smallbz,
        'picture':user.picture,
        'username':usernew.username,
        'themecount':themecount,
        'vipcount':vipcount,
        'dc':dc

    })

# @bbs.route('/')
# def index():
#     data = Category.query.all()
#     return render_template('html1.html',category=data)

@bbs.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        # password = hashlib.md5( password.encode('utf8')).hexdigest()
        res = User.query.filter(User.username==username,User.password==password).all()
        print(res)
        if res:
            session.permanent = True
            bbs.permanent_session_lifetime = timedelta(minutes=100)
            session['username'] = username
            return redirect(url_for('bbs.index'),)
        return redirect(url_for('bbs.index'))
    return redirect(url_for('bbs.index'))


@bbs.route('/list/<cid>')
def list_forum(cid):
    bz = Category.query.filter(Category.parentid==0).all()
        # bz = Category.query.filter(Category.id==cid).all()
    allBk = Category.query.filter(Category.parentid==0).all()
    # 小版块
    smallbz = Category.query.filter(Category.parentid!=0).all()
    last1 = Details.query.order_by(Details.addtime).limit(1).all()[0]
    user = User.query.get(1)
    dc = Details.query.filter(Details.tid==cid).all()
    return render_template('list.html',**{
        'category':bz,
        'allBk':allBk,
        'smalls':smallbz,
        'dtitle':dc,
        'last':last1,
        'picture':user.picture
    })

@bbs.route('/detail')
def detail():
    allBk = Category.query.filter(Category.parentid == 0).all()
    return render_template('detail.html',**{
        'allBk':allBk
    })

@bbs.route('/search')
def search():
    return render_template('search.html')
@bbs.route('/addc')
def addc():
    return render_template('addc.html')
@bbs.route('/admin')
def admin():
    return render_template('admin.html')
@bbs.route('/parenthome')
def list_parent():
    return render_template('parenthome.html')

@bbs.route('/reg',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        # return render_template('reg.html')
        allBk = Category.query.filter(Category.parentid == 0).all()
        return render_template('reg.html', **{
            'allBk': allBk
        })
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        email = request.form.get('email')
        allBk = Category.query.filter(Category.parentid == 0).all()

        # user = User.query.filter(User.username==username).all
        # if user:
        #     return jsonify({'msg': '此用户已存在'})
        user = User(username=username,password=password,email=email,udertype=1,
                    regtime=2019-6-16,lasttime=2019-6-6,regip=1,allowlogin=1)
        user.save()
        return redirect(url_for('bbs.index'))
        # return jsonify({'msg': 'ok'})
# @bbs.route('/setsession')
# def set_session():
#     session.permanent = True
#     bbs.permanent_session_lifetime = timedelta(minutes=10)
#     session['username'] = 'admin'
#     return "设置session"
@bbs.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return redirect(url_for('bbs.index'))
@bbs.route('/create')
def create_all():
    db.create_all()
    # data = User.query.filter(User.password=='999',User.username=='999').all()
    # print(data)
    return "创建成功"
#home网页...................

@bbs.route('/home')
def home():
    allBk = Category.query.filter(Category.parentid == 0).all()
    user = User.query.get(1).picture
    return render_template('home.html', **{
        'allBk': allBk,
        'picture': user
    })
@bbs.route('/homeqm')
def home_qm():
    allBk = Category.query.filter(Category.parentid == 0).all()
    user = User.query.get(1).picture
    return render_template('home_qm.html', **{
        'allBk': allBk,
        'picture': user
    })
@bbs.route('/homepass')
def home_pass():
    allBk = Category.query.filter(Category.parentid == 0).all()
    user = User.query.get(1).picture
    return render_template('home_pass.html', **{
        'allBk': allBk,
        'picture': user
    })
@bbs.route('/hometx/',methods=['GET','POST'])
def home_tx():

    return render_template('home_tx.html')
@bbs.route('/upload/',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # 获取文件上传对象
        obj = request.files.get('picture')
        if obj:
            # obj.filename 上传文件名
            path = os.path.join(current_app.config['UPLOAD_FOLDER'],obj.filename)
            print(path)
            obj.save(path)
            user = User.query.get(1)
            # 相对于static的路径
            user.picture = "upload/" + obj.filename
            db.session.add(user)
            db.session.commit()
            return "上传成功"
        return "上传失败"
    user = User.query.get(1)
    print(user.picture)
    # return render_template('home_tx.html',picture= user.picture)
    # return redirect(url_for('home_tx'),picture=user.picture)
    allBk = Category.query.filter(Category.parentid == 0).all()
    return render_template('home_tx.html', **{
        'allBk': allBk,
        'picture':user.picture
    })

# 验证码
@bbs.route('/yzm/')
def yzm():
    vc = VerfiCode()
    res = vc.output()
    # 把验证码字符粗存到session
    session['yzm'] = vc.code
    response = Response()
    response.status_code = 200
    response.headers['content-type'] = 'image/jpeg'
    response.data = res
    return response

@bbs.route('/showyzm/')
def show_yzm():
    return render_template('registered.html')


@bbs.route('/check')
def check_yzm():
    code = request.args.get('code')
    yzm = session.get('yzm')
    print(yzm,code)
    if yzm == code:
        return "验证成功"
    else:
        return "验证失败"