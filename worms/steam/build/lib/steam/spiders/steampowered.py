import scrapy
from ..items import BaseItem,SteamItem
from scrapy.http import Request


class SteampoweredSpider(scrapy.Spider):
    name = 'steampowered'
    allowed_domains = ['steampowered.com']
    # start_urls = ['http://steampowered.com/']
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0"}

    def start_requests(self):
            url = "http://store.steampowered.com/"
            yield Request(url, headers=self.headers)

    def parse(self, response):
        tmp = BaseItem()
        # item = SteamItem()
        tmp['content'] = response.xpath('//a[@class="search_result_row ds_collapse_flag"]').extract()
        # class ="search_result_row ds_collapse_flag"
        # content = response.xpath('//a[@class="search_result_row ds_collapse_flag"]').extract()
        # for i in range(len(content)):
            # item['steam_game_name'] = Handle.__getattr__("<span class=\"title\">(.+)</span>", content[i])
        # item['original_price'] = re\sponse.xpath('//strike/text()').extract()
        # item['discount_price'] = response.xpath('//div[@class="col search_price discounted responsive_secondrow"]/text()').extract()
        for i in range(len(tmp['content'])):
            item = SteamItem()
            item['steam_game_name'] = tmp.getattr("<span class=\"title\">(.+)</span>", i)
            item['comment_num'] = tmp.getattr("the (\S+) user", i).replace(',', '')
            item['favorable_rate'] = tmp.getattr("(\d+)%", i)
            item['discount'] = tmp.getattr("-(\d+)%", i)
            item['original_price'] = tmp.getattr("<strike>¥ (\d+)", i)
            item['discount_price'] = tmp.getattr("<br>¥ (\d+)", i)
            print(item['steam_game_name'])
            yield item
        for i in range(1, 11):
            url = "http://store.steampowered.com/search/?specials=1&page="+str(i)
            yield Request(url, callback=self.parse)
