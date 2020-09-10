from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json


class AliyunSMSAPI(object):
    APP_KEY_FIELD = 'ALIDAYU_APP_KEY'
    APP_SECRET_FIELD = 'ALIDAYU_APP_SECRET'
    SMS_SIGN_NAME_FIELD = 'ALIDAYU_SIGN_NAME'
    SMS_TEMPLATE_CODE_FIELD = 'ALIDAYU_TEMPLATE_CODE'
    REGION = 'cn-hangzhou'

    def __init__(self, app=None):
        if app:
            self.init_app(app)
        
    

    def init_app(self, app):
        config = app.config
        try:
            self.key = config[self.APP_KEY_FIELD]
            self.secret = config[self.APP_SECRET_FIELD]
            self.sign_name = config[self.SMS_SIGN_NAME_FIELD]
            self.template = config[self.SMS_TEMPLATE_CODE_FIELD]
            self.REMARK = "为CMS论坛的用户提供身份验证的验证码"
        except Exception as e:
            logging.error(e.args)
            raise ValueError('请填写正确的阿里云SMS配置！')
    

    def send_sms(self,telephone,**params):
        client = AcsClient(self.key, self.secret, self.REGION)
        dict_code = {"code":"1234"}
        
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', telephone)
        print(telephone)
        request.add_query_param('SignName', self.sign_name)
        request.add_query_param('TemplateCode', self.template)

        #code = params['code']
        #print("{\"code\":{0}}".format(params['code']))
        
        dict_code['code'] = params['code']

        request.add_query_param('TemplateParam', dict_code)

        response = client.do_action(request)
        # python2:  print(response) 
        print(str(response, encoding = 'utf-8'))
