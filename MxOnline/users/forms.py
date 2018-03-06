# coding:utf-8
# author:mini_panda
from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()  # 验证码


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()  # 验证


# 密码修改表单
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class ModifyPwdForm2(forms.Form):
    password1 = forms.CharField(required=True, min_length=5, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, min_length=5, widget=forms.PasswordInput)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # userprofile表
        fields = ['image']   # 修改的字段是image(头像)