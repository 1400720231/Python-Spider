from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:  # 内嵌Meta类
        model = Topic  # 关联model.Topic类
        fields = ['text']  # 验证"text"字段
        labels = {'text': ''}  # 提示信息；让django不要为字段text创建标签


class EntryForm(forms.ModelForm):  # 结合Model，继承django.forms.ModelForm
    class Meta:
        model = Entry
        '''
        field：Form对象中的一个字段。
        如：EmailField表示email字段，如果这个字段不是有效的email格式，就会产生错误。
        '''
        fields = ['text']  # 显示Entry中的'text' 字段，就是条目内容（text的内容）
        labels = {'text': ''} # 提示信息；让django不要为字段text创建标签
        # 自定义插件；针对文本框，文本区域框的宽度为80
        # Widget：用来渲染成HTML元素的工具，如：forms.Textarea对应HTML中的 < textarea > 标签
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}