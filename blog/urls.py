from django.conf.urls import url

from . import views

# 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间。
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # (?P[0-9]+) – 这部分比较复杂。它表示一个命名参数pk， 它会捕获url中的这部分然后将它赋值给pk参数传递给视图。 [0-9]表示这部分必须是数字，+表示至少1个数字，也可以多个数字。
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]