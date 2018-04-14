from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={
        'title': '我的主页',
        'welcome': '欢迎访问我的首页'
    })
