from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from utils.send_email import send_register_email


# 登陆视图
class CustomBackend(ModelBackend):
    # 自定义authenticate方法满足需求
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))  # 取出user对象
            if user.check_password(password):  # 因为django存储的密码是密文，不能直接取出password
                # 所以才用check_password的方法内部检验
                return user
        except Exception as e:
            return None


# 邮箱激活视图
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:  # 只要能筛选出来的都激活，因为有可能随机函数万一随机出来的字符串一样
            for record in all_records:
                email = record.email  # 获得email
                user = UserProfile.objects.get(email=email)  # 获得user信息
                user.is_active=True  # 是否激活改成True
                user.save()  # 保存到数据库
        return render(request, "login.html")


#  注册视图
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.get(email=user_name):  # 判断用户是否存在
                return render(request, "register.html", {'mes': '用户已存在'})
            else:
                pass_word = request.POST.get('password', '')
                user_profile = UserProfile()
                user_profile.username = user_name  # 这里的user_name是前端传过来的email
                user_profile.email = user_name
                user_profile.is_active = False  # 默认设置未激活
                # user_profile.set_password(pass_word)  # 保存密码
                user_profile.password = make_password(pass_word)  # 保存密码和上一行的操作意义一样
                user_profile.save()  # 这个就很尴尬了，非要加上force_inser=True才能从前端提交保存到数据库
                #但是我直接在后代文件中写save()就可以保存了，则会是为什么？？？
                # 然后几天之后我直接调用save方法居然又能行了，这是真的尴尬了
                send_register_email(user_name, 'register')
                return render(request, "login.html")
        else:
            return render(request, "login.html")


def LogoutView(request):
    logout(request)  # 登出
    # 登出后重定向到index页面
    return HttpResponseRedirect(
        reverse('index'))


# 登录视图
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:  # 是否激活，激活才让登录
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {'mes': '用户未激活'})
        else:
            return render(request, "login.html", {'msg': '用户名或者密码错误！', 'login_form': form})


class ForgetPwdViws(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", '')  # 获取前端穿过来的email值
            send_register_email(email, 'forget')   # 注册邮件发送完成，返回html
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


# 邮箱激活视图
class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:  # 只要能筛选出来的都激活，因为有可能随机函数万一随机出来的字符串一样
            for record in all_records:
                email = record.email  # 获得email
                return render(request, 'password_reset.html', {'email': email})
        return render(request, "login.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1')
            pwd2 = request.POST.get('password2')
            email = request.POST.get('email')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'mes':'密码不一致'})
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd2)
                user.save()
                return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'e mail': email, 'modify_form': modify_form})