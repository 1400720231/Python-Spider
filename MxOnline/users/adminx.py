#coding:utf-8
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):# 名字是固定写法
    enable_themes = True
    use_bootswatch = True



class GlobalSettings(object):  # 名字是固定写法
    site_title = "小熊的网站"
    site_footer = "小熊的公司"



class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # list_display陈列字段选项
    search_fields = ['code', 'email', 'send_type']  # search_fields搜索字段选项
    list_filter = ['code', 'email', 'send_type']  # list_filter 筛选字段选项




class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']  # list_display陈列字段选项
    search_fields = ['title', 'image', 'url', 'index']   # search_fields搜索字段选项
    list_filter = ['title', 'image', 'url', 'index', 'add_time'] # list_filter 筛选字段选项


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)