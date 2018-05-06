from django.shortcuts import render
from .tmp_models import Spider
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
import spider.scrapyd as spsd
from .models import Project

sd_req = spsd.get_scrapyd_request(server='10.147.17.51')


def project_manage(request):
    data = sd_req.project_list()
    return render(request, 'spider/project_manage.html', context={
        'data': data
    })





class IndexView(ListView):
    # model。将 model 指定为 Post，告诉 Django 我要获取的模型是 Post。
    model = Spider
    # template_name。指定这个视图渲染的模板。
    template_name = 'spider/base.html'
    # context_object_name。指定获取的模型列表数据保存的变量名。这个变量会被传递给模板。
    context_object_name = 'spider_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = "Spider"
        return context
