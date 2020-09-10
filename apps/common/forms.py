from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp, InputRequired
import hashlib

class SMSCaptchaForm(BaseForm):
    salt= 'jiangzy-love-caoxh'
    telephone = StringField(validators=[regexp(r'1[345789]\d{9}')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[InputRequired()])

    def validate(self, extra_validators=None):
        result = super(SMSCaptchaForm, self).validate()
        if not result:
            return False
        
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        sign2 = hashlib.md5((timestamp+telephone+self.salt).encode('utf-8')).hexdigest()
        print('客户端提交的sign:', sign)
        print('服务器生成的sign:', sign2)
        if sign == sign2:
            return True
        else:
            return False
        