from django.contrib import admin
from .models import Spider,Tag

# Register your models here.


#定制显示的内容
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'data_amount']


admin.site.register(Spider, PostAdmin)    #将定制的类放在后面
admin.site.register(Tag)