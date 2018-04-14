from django import forms
from .models import Comment


# 通过调用这个类的一些方法和属性，Django 将自动为我们创建常规的表单代码
class CommentForm(forms.ModelForm):
    # 我们在表单的内部类Meta里指定一些和表单相关的东西。
    # model = Comment表明这个表单对应的数据库模型是Comment类。
    # fields = ['name', 'email', 'url', 'text']指定了表单需要显示的字段，这里我们指定了name、email、url、text需要显示。
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']