from django.conf.urls import url
from . import views


app_name = 'homepage'
urlpatterns = [
    url(r'^$', views.index, name='home_index'),
    url(r'^demo$', views.demo, name='home_demo'),
]