from django.db import models

# Create your models here.
# steam_game_name,comment_num,favorable_rate,discount,original_price,discount_price


# camelCase叫做“骆驼拼写法”，是指在英语中，依靠单词的大小写拼写复合词的做法。
class GameItem(models.Model):
    steam_game_name = models.CharField(max_length=100)
    comment_num = models.IntegerField()
    favorable_rate = models.IntegerField()
    discount = models.IntegerField()
    original_price = models.FloatField()
    discount_price = models.FloatField()
