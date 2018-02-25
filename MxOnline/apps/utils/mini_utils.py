# coding:utf-8
# author:mini_panda
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

"""
一个基于类继承的装饰器类，因为view下面是类的方法写的不是函数
若是函数就直接用@login_required就好了
"""


class LoginRequireMixin(object):
    """
    method_decorator 把装饰器函数转化成装饰器方法
    """
    @method_decorator(login_required(login_url='/login/'))  # 没有登录的话就跳转到login页面
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequireMixin, self).dispatch(request, *args, **kwargs)
    # super方法的意思就是调用装饰函数

"""
method_decorator()源码中的注释：
def method_decorator(decorator, name=''):
    
    Converts a function decorator into a method decorator
    
    # 'obj' can be a class or a function. If 'obj' is a function at the time it
    # is passed to _dec,  it will eventually be a method of the class it is
    # defined on. If 'obj' is a class, the 'name' is required to be the name
    # of the method that will be decorated.
    
    
    obj可以是一个类或一个函数。如果在传递到dec的时候“obj”是一个函数，
    那么它最终将成为它定义的类的一个方法。
    如果“obj”是一个类，那么“name”就是要被修饰的方法的名称(指类中的函数方法)。
"""