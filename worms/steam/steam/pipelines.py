# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from .items import SteamItem


class SteamPipeline(object):
    def __init__(self):
        self.file = open("/Users/vallzey/Downloads/test1.csv", "a")
        self.file.write(
            "游戏名" + "," + "评论数" + "," + "好评率(%)" + "," + "折扣(%)" + "," + "原价(¥)" + "," + "现价(¥)" + "\n")

    def process_item(self, item, spider):
        # game = SteamItem()
        # for i in range(0, 25):
            # name = item["steam_game_name"][i]
            # game['steam_game_name'] = item.getattr("<span class=\"title\">(.+)</span>", i)
            # game['comment_num'] = item.getattr("the (\S+) user", i).replace(',','')
            # game['favorable_rate'] = item.getattr("(\d+)%", i)
            # game['discount'] = item.getattr("-(\d+)%", i)
            # game['original_price'] = item.getattr("<strike>¥ (\d+)", i)
            # game['discount_price'] = item.getattr("<br>¥ (\d+)", i)
        # self.file.write(item['steam_game_name']+","+item['comment_num']+","+item['favorable_rate']+","+item['discount']+","+item['original_price']+","+item['discount_price']+'\n')
        item.save()
        return item

    def close_spider(self, spider):
        self.file.close()
        print("End")
