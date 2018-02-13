#coding=utf-8
"""定义learning_log的URL Patterns"""
from django.conf.urls import url
from . import views  #.表示当前learning_logs的文件夹
urlpatterns = [
    #主页
    url(r'^$',views.index, name='index'),  # r'^$' 表示首页127.0.0:8000/   也可以用name="index"表示
    #显示所有主题
    url(r'^topics/$', views.topics, name='topics'),  # r'^topics/$' 表示127.0.0.1:8000/topics用 name='topics'也可以表示
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),  # 将整数的匹配值赋值给topic_id
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]
'''
    举例：url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
    
    1、这里的name='edit_entry' 就是指的url地址127.0.0.1:8000/edit_entry/(\d),
    在html文件中啊<a href="learning_logs:edit_entry"> 就是指这里的name="edit_entry"中的edit_entry,
    即跳转到127.0.0.1:8000/edit_entry/(\d)
    2、当访问地址是127.0.0.1/edit_entry/1/ 的时候/1/中的1将会被捕获给topic_id=1,
    然后传给views.edit_entry(request,topic_id)中的topic_id,
    '''