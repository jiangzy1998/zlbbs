import os

DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = '123456789'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'zlbbs'

SECRET_KEY = "Hard to guess"

# PERMANENT_SESSION_LIFETIME =

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


CMS_USER_ID = "CMS_USER_ID"
FRONT_USER_ID = 'SDFASFSD2343205KSDLFD'



# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.163.com"
MAIL_PORT = '465'
# MAIL_USE_TLS = True 
MAIL_USE_SSL = True
MAIL_USERNAME = "1876268353@163.com"
MAIL_PASSWORD = "YHPVDXIARKEAPYO"
MAIL_DEFAULT_SENDER = "1876683053@163.com"


ALIDAYU_APP_KEY = 'LTAI4GJYyktHAqAgnEsPBtd'
ALIDAYU_APP_SECRET = 'nQLRuIfrfatylyw5jEtzhv3eqxmBg'
ALIDAYU_SIGN_NAME = 'CMS论坛'
ALIDAYU_TEMPLATE_CODE = 'SMS_19789449'


# UEditor的相关配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "0eDT20SZZfWTxLkbR61thHh5SOywA3W3RiJAZY"
UEDITOR_QINIU_SECRET_KEY = "BIdoAL7J9kxLdjSlnB1vjYg7F-rZQxYJ3HxjTP"
UEDITOR_QINIU_BUCKET_NAME = "jzypro-cms2"
UEDITOR_QINIU_DOMAIN = "http://qfri4iq2f.hd-bkt.clouddn.com/"


# flask-paginate的相关配置
PER_PAGE = 10

# celery相关的配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

# memache client
MEMACHE_CLIENT = "127.0.0.1:11211"
