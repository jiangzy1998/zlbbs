from flask import Blueprint, make_response, request, jsonify
from utils.captcha import Captcha
from utils import zlcache, restful
from io import BytesIO
from .forms import SMSCaptchaForm
from utils.captcha import Captcha
from exts import alidayu
import string
import random
import qiniu
from tasks import send_sms_captcha


bp = Blueprint("common", __name__, url_prefix="/c")

@bp.route('/')
def index():
    return "common index"


@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        print('发送的短信验证码是:', captcha)
        send_sms_captcha(telephone,captcha)
        zlcache.set(telephone, captcha)
        return restful.success()
    else:
        return restful.params_error(message='参数错误!')


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    zlcache.set(text.lower(), text.lower())
    print(zlcache.get(text.lower()))
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


@bp.route("/uptoken/")
def uptoken():
    access_key = '0eDT20SZZfWTxLsekbR61thHh5SOywA3W3RiJAZY'
    secret_key = 'BIdoAL7J9kxLdj3jSlnB1vjYg7F-rZQxYJ3HxjTP'

    q = qiniu.Auth(access_key, secret_key)

    bucket = 'jzypro-cms2'
    token = q.upload_token(bucket)
    return jsonify({'uptoken':token})
