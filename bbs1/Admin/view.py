import hashlib

from flask import Blueprint, render_template, request, redirect, url_for
from App.model import *

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/')
def index():
    return  render_template('admin/admin_index.html')

@admin.route('/category/',methods=['GET','POST'])
def category():
    # 找到大版块的内容
    bigblock_all = Category.query.filter(Category.parentid == 0).all()
    # 找到所有的小版块
    smallblock_all = Category.query.filter(Category.parentid != 0).all()
    if request.method == "POST":
        data = request.form
        for rec in data:
            recode = data.getlist(rec) #['1', '0', 'PHP技术交流'] ['6', '0', '进阶讨论', ''] [id,orderby,classname,compera]
            if recode[0] != "提交":
                for bigblock in bigblock_all:
                    if int(recode[0]) == bigblock.cid:
                        bigblock.classname = recode[2]
                        bigblock.orderby = recode[1]
                        db.session.commit()
                        break
                for smallblock in smallblock_all:
                    if int(recode[0]) == smallblock.cid:
                        smallblock.compere = recode[3]
                        smallblock.classname = recode[2]
                        smallblock.orderby = recode[1]
                        db.session.commit()
                        break
    return render_template('admin/admin_category.html', **{"bigblock_all": bigblock_all,
                                                           "smallblock_all": smallblock_all})
# 用户管理
@admin.route('/member/',methods=["GET","POST"])
def member():
    user_all = User.query.filter().all()
    if request.method == "GET":
        return render_template('admin/admin_member.html',**{"user_all":user_all})
    data = request.form
    for rec in data:
        recode = data.getlist(rec)
        if recode[0] != '删除':
            user = User.query.filter(User.id==recode[0]).first()
            db.session.delete(user)
            post_del = Details.query.filter(Details.authorid==user.id).all()
            print(post_del)
            for post in post_del:
                db.session.delete(post)
            reply_del = Details.query.filter(Details.classid==user.id).all()
            print(reply_del)
            for reply in reply_del:
                db.session.delete(reply)
            db.session.commit()
    return redirect(url_for('admin.member'))

    # return  render_template('admin/admin_member.html',**{"user_all":user_all})


@admin.route('/detail/')
def detail():
    return  render_template('admin/admin_detail.html')


@admin.route('/site/')
def site():
    return  render_template('admin/admin_main.html')
# 友情链接
@admin.route('/link/')
def link():
    return  render_template('admin/admin_link.html')

@admin.route('/lockip/')
def lockip():
    return  render_template('admin/admin_lock_ip.html')

# 板块管理
@admin.route('/addcategory/',methods=["GET","POST"])
def addcategory():
    # 找到大版块的内容
    bigblock_all = Category.query.filter(Category.parentid == 0).all()
    # 找到所有的小版块
    smallblock_all = Category.query.filter(Category.parentid != 0).all()
    if request.method == "POST":
        classname = request.form.get("classname")
        parentid = request.form.get('parentid')
        print(parentid)
        new_post = Category(classname=classname,parentid=parentid)
        db.session.add(new_post)
        db.session.commit()
    return render_template("admin/admin_category_add.html",**{"bigblock_all": bigblock_all,
                                                           "smallblock_all": smallblock_all})
# 删帖
@admin.route('/deletepost/')
def deletepost():
    return  render_template('admin/admin_detail_del.html')


@admin.route('/reply/')
def reply():
    return  render_template('admin/admin_detail_hf.html')

@admin.route('/recyle/')
def recyle():
    return  render_template('admin/admin_detail_hf_del.html')

# 管理员登录
@admin.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('admin/admin_login.html')
    else:
        admin_username = request.form.get("admin_username")
        admin_password = request.form.get("admin_password")
        # admin_password = hashlib.sha1(admin_password.encode("utf-8")).hexdigest()
        # 找到该管理员用户对象
        userobj = User.query.filter(admin_username==User.username).first()
        if userobj:
            if userobj.udertype == 1 and userobj.password == admin_password:
                return render_template("admin/admin_index.html")
        return  render_template("admin/admin_login.html")

@admin.route("/adminstrate/")
def adminstrate():
    return "adminstrate"

# 退出
@admin.route('/logout/')
def logout():
    return  '退出登录'

@admin.route('/dolink/')
def dolink():
    return  '退出登录'
