from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    # 在创建多对一的关系的, 需要在Foreign的第二参数中加入on_delete = models.CASCADE
    # 主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
