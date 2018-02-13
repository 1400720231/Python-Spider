from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)  # charfield 就是数据库徳var后者charvar，max_length表示最大长度
    date_added = models.DateTimeField(auto_now_add=True)  # 每当用户创建新主题的时候，自动生成时间戳
    owner = models.ForeignKey(User)  # 添加owner字段建立与User的外键关系
    # 添加owner后要记得数据的迁移，不然浏览器Topics点击会报错

    def __str__(self):
        """返回 models 的字符串的表示"""
        return self.text
        # 进入后台管理就可以看到这里的self.text ,比如python字典。python列表等创建的主题（self.text）


class Entry(models.Model):
    """学到的有关某个主题具体的知识，是topic的具体内容"""
    # 给topic添加一个外键，或者说Topic是topic的外键，所以才有一个topic下有好多个条目
    # 但是打开数据库表，新建的entry中没有topic这个字段，只有id,text，date_added
    topic = models.ForeignKey(Topic)
    text = models.TextField()   #
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # Meta应该是内置参数，好多都是这么写的，需要去查一查
        verbose_name_plural = "entries"  # verbose_name_plural是Meta下的一个option，
        # 表示类Entry的复数形式为entries，在admin用户登陆可以看到Entries(默认大写)

    def __str__(self):
        """返回 model 的字符串表示"""
        return self.text[:50] + "..."
        # 点击进入一个topic的时候，某个内容可能会很长，只显示前50个字符


'''
Django 模型类的Meta是一个内部类，它用于定义一些Django模型类的行为特性
 
  1、ordering
这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的。
这是一个字符串的元组或列表，没有一个字符串都是一个字段和用一个可选的表明降序的'-'构成。
当字段名前面没有'-'时，将默认使用升序排列。使用'?'将会随机排列
    ordering=['order_date'] # 按订单升序排列
    ordering=['-order_date'] # 按订单降序排列，-表示降序
    ordering=['?order_date'] # 随机排序，？表示随机
    ordering=['-pub_date','author'] # 以pub_date为降序，在以author升序排列

  2、verbose_name_plural
这个选项是指定，模型的复数形式是什么，比如：
verbose_name_plural = "学校"
如果不指定Django会自动在模型名称后加一个’s’
用superuser登陆可以看到区别
'''