from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        author = Author.objects.filter(name=self.name)
        if len(author) > 0:
            return author[0]
        else:
            return super(Author, self).save()


class Origin(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    #标题
    title = models.CharField(max_length=70)
    # 创建时间,创建的时候自动获取
    created_time = models.DateTimeField(auto_now=True)
    #作者
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    #分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    #标签
    tags = models.ManyToManyField(Tag, blank=True)
    #摘要
    excerpt = models.CharField(max_length=200, blank=True)
    #主体
    body = models.TextField(null=True)
    #原网址
    url = models.CharField(max_length=200, blank=True)
    #来源网站
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, null=True)
    # 该类型的值只允许为正整数或 0
    views = models.PositiveIntegerField(default=0)
    # source = models

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    '''
    于是 reverse 函数会去解析这个视图函数对应的 URL，我们这里 detail 对应的规则就是 post/(?P<pk>[0-9]+)/ 这个正则表达式，
    而正则表达式部分会被后面传入的参数 pk 替换，所以，如果 Post 的 id（或者 pk，这里 pk 和 id 是等价的） 是 255 的话，
    那么 get_absolute_url 函数返回的就是 /post/255/ ，这样 Post 自己就生成了自己的 URL。
    '''
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    '''
    Django 允许我们在 models.Model 的子类里定义一个 Meta 的内部类，
    这个内部类通过指定一些属性来规定这个类该有的一些特性，例如在这里我们要指定 Post 的排序方式。
    '''
    class Meta:
        '''
        定文章排序方式，['-created_time'] 指定了依据哪个属性的值进行排序，这里指定为按照文章发布时间排序，
        且负号表示逆序排列。列表中可以用多个项，比如 ordering = ['-created_time', 'title'] ，
        那么首先依据 created_time 排序，如果 created_time 相同，则再依据 title 排序。
        这样指定以后所有返回的文章列表都会自动按照 Meta 中指定的顺序排序，
        因此可以删掉视图函数中对文章列表中返回结果进行排序的代码了。
        '''
        ordering = ['-created_time']
