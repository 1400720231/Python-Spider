# coding:utf-8
# author:mini_panda
from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView
urlpatterns =[
    # 搜游课程页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail')
]