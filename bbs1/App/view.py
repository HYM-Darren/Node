from flask import Blueprint, render_template, session,jsonify,current_app
from flask import Flask, make_response, request, redirect, url_for, session,Response
import time
import os
from datetime import timedelta
from .forms import RegisterForm, UploadForm
from sqlalchemy import func

from .VerfiCode import VerfiCode
from .model import *
from ext import db
bbs = Blueprint('bbs',__name__)

@bbs.route('/')
@bbs.route('/<int:cid>',methods=['GET','POST'])
def index(cid=0):

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

        if res:
            session.permanent = True
            bbs.permanent_session_lifetime = timedelta(minutes=100)
            session['username'] = username
            return redirect(url_for('bbs.index'),)
        return redirect(url_for('bbs.index'))
    return redirect(url_for('bbs.index'))

@bbs.route('/list')
@bbs.route('/list/<cid>')
def list_forum(cid):
    bz = Category.query.filter(Category.parentid==0).all()
        # bz = Category.query.filter(Category.id==cid).all()
    allBk = Category.query.filter(Category.parentid==0).all()
    # 小版块
    smallbz = Category.query.filter(Category.parentid!=0).all()
    sname = Category.query.filter(Category.id==cid).first()
    sunm = Details.query.filter(Details.tid==cid).count()
    last1 = Details.query.order_by(Details.addtime).limit(1).all()[0]
    user = User.query.get(1)
    dc = Details.query.filter(Details.tid==cid).all()
    page = int(request.args.get('page', 1))
    pagination = User.query.paginate(page, 10)
    # jhimg = Details.query.filter(Details.elite).all()
    # print(jhimg)
    # juing = Details.query.filter(Details.elite)
    return render_template('list.html',**{
        'category':bz,
        'allBk':allBk,
        'smalls':smallbz,
        'dtitle':dc,
        'last':last1,
        'picture':user.picture,
        'sname':sname,
        'sunm':sunm,
        'pagination' : pagination

    })


@bbs.route('/detail/<cid>',methods=['GET','POST'])
@bbs.route('/detail/',methods=['GET','POST'])
def detail(cid):
    allBk = Category.query.filter(Category.parentid == 0).all()
    user = User.query.get(1).picture
    sutit1 = Details.query.filter(Details.id == cid).first()
    # sutit = Details.query.filter(Details.tid==Details.id)
    dclass = Details.query.filter(Details.classid == cid).all()
    tt = Details.query.filter(Details.classid == cid).count()
    return render_template('detail.html', **{
        'sutit1':sutit1,
        'tt':tt,
        'dclass':dclass,
        'allBk': allBk,
        'picture': user,
        "cid":cid
    })
@bbs.route('/jinghua/<cid>')
def jing_hua(cid):
    sutit1 = Details.query.filter(Details.id == cid).first()
    sutit1.elite = 1
    sutit1.save()
    return redirect(url_for('bbs.detail',cid=sutit1.id))
@bbs.route('/reply/<cid>',methods=['GET','POST'])
def reply(cid):
    content = request.form.get('message')

    reuser = Details(title="dar", content=content, rate=1, first=10, tid=2, authorid=10, addtime=2015 - 5 - 8,addip=10, classid=cid, replycount=5, hits=5, istop=1, elite=1, ishot=1, isdel=5, isdisplay=0)
    reuser.save()
    hui = Details.query.order_by(-Details.id).first()
    return redirect(url_for('bbs.detail',cid=hui.classid))
@bbs.route('/search')
def search():
    return render_template('search.html')
@bbs.route('/addc',methods=['GET','POST'])
def addc():
    if request.method == 'GET':
        allBk = Category.query.filter(Category.parentid == 0).all()
        user = User.query.get(1).picture
        # sutit = Details.query.order_by(-Details.id).first()

        return render_template('addc.html', **{
        # 'sutit': sutit,
        'allBk': allBk,
        'picture': user
    })
    elif request.method == 'POST':
        subject = request.form.get('subject')
        content = request.form.get('content')
        price = request.form.get('price')

        user = Details(title=subject, content=content, rate=price, first=10,tid=2,authorid=10,addtime=2015-5-8,addip=10,classid=2,replycount=5,hits=5,istop=1,elite=1,ishot=1,isdel=5,isdisplay =0)
        user.save()
        sutit = Details.query.order_by(-Details.id).first()
        return redirect(url_for('bbs.detail',cid=sutit.id))

@bbs.route('/parenthome')
def list_parent():
    return render_template('parenthome.html')

@bbs.route('/reg',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        allBk = Category.query.filter(Category.parentid == 0).all()
        form = RegisterForm()
        return render_template('reg.html', **{
            'form':form,
            'allBk': allBk
        })
    elif request.method == 'POST':
        form = RegisterForm()
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            repassword = request.form.get('repassword')
            email = request.form.get('email')
            data = db.session.query(User).filter(User.username == username).all()
            # print(username,1111)
            user = User(username=username,password=password,email=email,udertype=1,regtime=2019-6-16,lasttime=2019-6-6,regip=1,allowlogin=1)
            user.save()

            return redirect(url_for('bbs.index'))
        return render_template('reg.html', form=form)

@bbs.route('/deletereply/<cid>')
def delete_reply(cid):
    de1 = Details.query.filter(Details.id == cid).first()
    de1.delete()
    return redirect(url_for('bbs.detail',cid=de1.classid))



@bbs.route('/delete/')
def delete():
    # print(session.get('username'))
    session.pop('username')
    # print(session.get('username'))
    return redirect(url_for('bbs.index'))
@bbs.route('/create')
def create_all():
    db.create_all()
    # data = User.query.filter(User.password=='999',User.username=='999').all()
    # print(data)
    return "创建成功"
#home网页...................

@bbs.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        realname = request.form.get("realname")
        sex = request.form.get("sex")
        place = request.form.get("sex")
        qq = request.form.get("qq")
        username=session['username']
        user = User.query.filter(User.username == username).first()
        user.realname = realname
        user.place = place
        user.qq = qq
        user.save()
    allBk = Category.query.filter(Category.parentid == 0).all()
    user = User.query.get(1).picture
    return render_template('home.html', **{
        'allBk': allBk,
        'picture': user
    })
@bbs.route('/homeqm',methods=['GET','POST'])
def home_qm():
    if request.method == 'POST':
        autograph = request.form.get("content")
        username = session['username']
        user = User.query.filter(User.username == username).first()
        user.autograph = autograph
        user.save()
        # print(autograph)
    allBk = Category.query.filter(Category.parentid == 0).all()
    user = User.query.get(1).picture
    return render_template('home_qm.html', **{
        'allBk': allBk,
        'picture': user
    })
@bbs.route('/homepass',methods=['GET','POST'])
def home_pass():
    if request.method == 'POST':
        oldpassword = request.form.get('oldpassword')
        newpassword = request.form.get('newpassword')
        newpassword2 = request.form.get('newpassword2')
        username = session['username']
        user = User.query.filter(User.username == username).first()
        if oldpassword == user.password:
            if newpassword2 == newpassword:
                user.password = newpassword
                user.save()
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
            # print(path)
            obj.save(path)
            user = User.query.get(1)
            # 相对于static的路径
            user.picture = "upload/" + obj.filename
            db.session.add(user)
            db.session.commit()
            return "上传成功"
        return "上传失败"
    user = User.query.get(1)
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
    # print(yzm,code)
    if yzm == code:
        return "验证成功"
    else:
        return "验证失败"

# 捕获500的错误
@bbs.app_errorhandler(500)
def file_notfound(error):
    return render_template('500.html')


# 捕获404的错误
@bbs.app_errorhandler(404)
def file_notfound(error):
    return render_template('404.html')