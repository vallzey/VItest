import urllib.request
import ssl
from lxml import etree
from resource_library.models import Post, Category, Tag, Author, Origin


class CsdnExplorer(object):
    def __init__(self, headers=None, charset=None):
        self.headers = headers or \
                       {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 "
                                      "(KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"}
        self.charset = charset or "utf-8"

    def get_content(self, url):
        context = ssl._create_unverified_context()
        # 因为url可以使用的字符有限制，所有其他字符都应该使用url编码，你应该先把中文编码成 % XX这样的形式再拼起来
        # url = urllib.parse.quote(url)
        opener = urllib.request.build_opener()
        # 模拟浏览器
        opener.addheaders = [self.headers]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url, context=context).read().decode(self.charset)
        return data


class PostSave(object):
    def __init__(self):
        self.post = Post()
        self.author = Author()


    def save_from_html(self, data):
        selector = etree.HTML(data)
        # 使用starts - with方法提取div的id标签属性值开头为a的div标签

        self.author.name = selector.xpath('//a[@id="uid"]/text()')[0]
        author = self.author.save()

        self.post.title = selector.xpath('//h1[@class="csdn_top"]/text()')[0]
        self.post.excerpt = selector.xpath('//meta[@name="description"]/@content')[0]
        self.post.body = selector.xpath('//div[@class="htmledit_views"]')[0].xpath('string(.)').strip()
        self.post.author = author
        return self.post
        # try:
        #     file = open('/Users/vallzey/Downloads/test2', 'w', encoding='utf-8')
        #     file.write(data)
        # finally:
        #     file.close()