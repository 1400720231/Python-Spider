# coding:utf-8
# author:mini_panda
from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="info"),
    # 头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    # 用户个人中心修密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 验证并修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
]