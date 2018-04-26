from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post,Category


# Create your views here.


class IndexView(ListView):
    # model。将 model 指定为 Post，告诉 Django 我要获取的模型是 Post。
    model = Post
    # template_name。指定这个视图渲染的模板。
    template_name = 'resource_library/resource_index.html'
    # context_object_name。指定获取的模型列表数据保存的变量名。这个变量会被传递给模板。
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 10
