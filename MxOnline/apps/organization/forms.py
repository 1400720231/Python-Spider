# coding:utf-8
# author:mini_panda
from django import forms
import re

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']


    """
    自定义验证字段的方法
    定义一个验证mobile是否合法的函数,函数名必须以clean开头，
    加上要验证的字段名，用下划线链接：clean_mobile
    """
    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']  # cleaned_data方法就是把实例的对象转化成字典
        rex = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'  # 手机号正则表达式
        p = re.compile(rex)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号非法', code="invalid mobile")
        # ValidationError()两个参数， 一个是message错误信息， 一个是自定义状态码,默认code=None
        # 错误甩给了forms，所以调试的时候views中的forms.errors会包含这一点，