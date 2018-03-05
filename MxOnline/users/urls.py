# coding:utf-8
# author:mini_panda
from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView
urlpatterns = [
    # 用户信息
    url(r'info/$', UserInfoView.as_view(), name="info"),
    # 头像上传
    url(r'image/upload/$', UploadImageView.as_view(), name="image_upload")


]