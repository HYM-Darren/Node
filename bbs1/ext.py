from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_uploads import UploadSet,IMAGES
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
moment = Moment()
# 上传对象
photos = UploadSet('photos',IMAGES)
bootstrap = Bootstrap()
