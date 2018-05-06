from django.contrib import admin
from .tmp_models import Spider, Tag, Type, Status

# Register your models here.


#定制显示的内容
class SpiderAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'status', 'data_amount']


admin.site.register(Spider, SpiderAdmin)    #将定制的类放在后面
admin.site.register(Tag)
admin.site.register(Type)
admin.site.register(Status)
