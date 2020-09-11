from ..forms import BaseForm
from wtforms import StringField, IntegerField
from wtforms.validators import Regexp, EqualTo, ValidationError
from wtforms.validators import InputRequired
from utils import zlcache
from .models import FrontUser


class ResetPwdForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}",message='请输入正确格式的手机号码！')])
    sms_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式的短信验证码！')])
    password1 = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}",message='请输入正确格式的密码！')])
    password2 = StringField(validators=[EqualTo("password1",message='两次输入的密码不一致！')])
    graph_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式的短信验证码！')])

     # 短信验证码校验
    def validate_sms_captcha(self,field):
        sms_captcha = field.data
        telephone = self.telephone.data

        if sms_captcha != '1111':
            sms_captcha_mem = zlcache.get(telephone)
            if not sms_captcha_mem or sms_captcha_mem.lower() != sms_captcha.lower():
                print(sms_captcha, sms_captcha_mem)
                raise ValidationError(message='短信验证码错误！')


    def validate_graph_captcha(self,field):
        graph_captcha = field.data

        if graph_captcha != '1111':
            graph_captcha_mem = zlcache.get(graph_captcha.lower())
            if not graph_captcha_mem:
                print(graph_captcha_mem)
                raise ValidationError(message='图形验证码错误！')


# 注册表单校验
class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}",message='请输入正确格式的手机号码！')])
    sms_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式的短信验证码！')])
    username = StringField(validators=[Regexp(r".{2,20}",message='请输入正确格式的用户名！')])
    password1 = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}",message='请输入正确格式的密码！')])
    password2 = StringField(validators=[EqualTo("password1",message='两次输入的密码不一致！')])
    graph_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式的短信验证码！')])

    # # 手机号码校验
    # def validate_telephone(self, field):
    #     input_telephone = field.data
    #     old_telephone = FrontUser.query.get(input_telephone)
    #     if old_telephone:
    #         raise ValidationError(message="手机号码已注册！")
    
    # 短信验证码校验
    def validate_sms_captcha(self,field):
        sms_captcha = field.data
        telephone = self.telephone.data

        if sms_captcha != '1111':
            sms_captcha_mem = zlcache.get(telephone)
            if not sms_captcha_mem or sms_captcha_mem.lower() != sms_captcha.lower():
                print(sms_captcha, sms_captcha_mem)
                raise ValidationError(message='短信验证码错误！')


    def validate_graph_captcha(self,field):
        graph_captcha = field.data

        if graph_captcha != '1111':
            graph_captcha_mem = zlcache.get(graph_captcha.lower())
            if not graph_captcha_mem:
                print(graph_captcha_mem)
                raise ValidationError(message='图形验证码错误！')
    

class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}", message='请输入正确格式的手机号码！')])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}", message='请输入正确格式的密码！')])
    remember = StringField()


class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id！')])


class AddCommentForm(BaseForm):
    content = StringField(validators=[InputRequired(message='请输入评论内容！')])
    post_id = IntegerField(validators=[InputRequired(message='请输入帖子id！')])