# coding:utf-8
# author:mini_panda
from django.conf.urls import url, include
from .views import UserInfoView
urlpatterns = [
    # 用户信息
    url(r'info/$', UserInfoView.as_view(), name="info")


]