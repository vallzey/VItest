# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from spider_instences.models import GameItem
from scrapy_djangoitem import DjangoItem
import re


class BaseItem(scrapy.Item):
    content = scrapy.Field()

    def getattr(self, regular, i):
        attr = re.compile(regular).findall(self['content'][i])
        if len(attr) > 0:
            return attr[0]
        else:
            return ""


class SteamItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = GameItem
