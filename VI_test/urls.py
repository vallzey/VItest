"""VI_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path(r'home/', include('homepage.urls')),
    path('admin/', admin.site.urls),
    # 这里是做一个拼接 r''表示原生字符串
    path(r'blog/', include('blog.urls')),
    path(r'comment/', include('comments.urls')),
    path(r'spider/', include('spider.urls')),
    path(r'data_mining/', include('data_mining.urls')),
]
