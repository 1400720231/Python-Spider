 from django.conf.urls import url
# django默认的登陆view，需要传参{'template':'...html'},
# 不然就是默认的register/login.html,需要你自己创建
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]

'''
{'template_name': 'users/login.html'},因为调用的是django的logout，所以没有
views.logout,页就不能再views.logout指定html了，所以直接指定logout将会把
信息渲染到users/login.html上，template_name即为html名字的参数，
users/login.html为路径，其中users为app下的对应的模板文件夹名字，
即users/templates/users 
'''