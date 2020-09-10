from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from utils.aliyun_sms import AliyunSMSAPI

db = SQLAlchemy()
mail = Mail()
alidayu = AliyunSMSAPI()