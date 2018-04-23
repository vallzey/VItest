from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    # 该类型的值只允许为正整数或 0
    views = models.PositiveIntegerField(default=0)
    source = models

    # 重写save方法
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

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