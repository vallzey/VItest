from django.conf.urls import url

from . import views

app_name = 'spider'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='spider_index'),
    url(r'index', views.IndexView.as_view(), name='spider_list'),
]
