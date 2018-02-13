from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm



# 注销
def logout_view(request):
    logout(request)  # 登出
    # 登出后重定向到index页面
    return HttpResponseRedirect(
        reverse('learning_logs:index'))


# 注册
def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # get方法的时候，定义一个空的注册表单准备返回到template_name上面，和登陆的流程的是一样的
        form = UserCreationForm()   # 登陆的时候是form=LoginForm，这里是UserCreationForm，一样的逻辑
    else:
        # 处理填好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():  # 数据是有效的，该有的有
            new_user = form.save()  # 保存注册信息
            # 用户自动登陆，再重定向定向到主页，password1意思是注册一般输入两次密码的第一个
            # authenticate判断是否是本网站的用户，是返回User的一个实例对象给authenticate_user，不是就返回None
            authenticate_user = authenticate(username=
                new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)  # 登录进去
            return HttpResponseRedirect(reverse('learning_logs:index'))
            #  返回到index页面
    context = {'form': form}
    return render(request, 'users/register.html', context)