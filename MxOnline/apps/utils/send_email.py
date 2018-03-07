# coding:utf-8
# author:mini_panda
import random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM


# 随机字符串函数
def random_str(random_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(random_length):  # 循环8次
        str += chars[random.randint(0, length)]  #随机肌肤穿拼接８次
    return str


# 把随机字符串和对应的邮箱保存在数据库，并发送邮件
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_titile = ''
    email_body = ''
    if send_type == 'register':
        email_titile = '小熊的网站的激活链接'
        email_body = '请点击下面的链接激活你的账号：http:127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(subject=email_titile, message=email_body, from_email=EMAIL_FROM, recipient_list=[email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_titile = '小熊的网站密码重置链接'
        email_body = '请点击下面的链接激活你的账号：http:127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(subject=email_titile, message=email_body, from_email=EMAIL_FROM, recipient_list=[email])
        if send_status:
            pass
    elif send_type == 'update_email':
        email_titile = '小熊的网站的邮箱修改验证码'
        email_body = '你的邮箱验证码为：{0}'.format(code)
        send_status = send_mail(subject=email_titile, message=email_body, from_email=EMAIL_FROM, recipient_list=[email])
        if send_status:
            pass