from django.contrib import admin
from .models import Category,Tag,Post

# Register your models here.


#定制显示的内容
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Post, PostAdmin)    #将定制的类放在后面
admin.site.register(Category)
admin.site.register(Tag)