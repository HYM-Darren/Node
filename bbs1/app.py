import os
from flask import Flask
from flask_script import Manager
from ext import db
from flask_uploads import configure_uploads,patch_request_class,IMAGES
from App.model import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rock1204@127.0.0.1:3306/FlaskModel"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '3322FDF'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),'static/upload')
app.config['UPLOADED_PHOTOS_DEST'] =  os.path.join(os.getcwd(),'static/upload')

db.init_app(app)

manager = Manager(app)

from App.view import bbs
from Admin.view import admin

app.register_blueprint(bbs)
app.register_blueprint(admin)
if __name__ == '__main__':
    # app.run()
    manager.run()