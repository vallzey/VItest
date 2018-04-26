import urllib.request
import ssl
from lxml import etree
from resource_library.models import Post, Category, Tag, Author, Origin


class CsdnSpider:
    def __init__(self):
        self.post = Post()
        self.category = Category()

    def get_content(self, url):
        context = ssl._create_unverified_context()
        # 因为url可以使用的字符有限制，所有其他字符都应该使用url编码，你应该先把中文编码成 % XX这样的形式再拼起来
        # url = urllib.parse.quote(url)
        opener = urllib.request.build_opener()
        # 模拟浏览器
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"}
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url, context=context).read().decode("utf-8", "ignore")
        return data

    def save(self, url):
        data = self.get_content(url)
        selector = etree.HTML(data)
        # 使用starts - with方法提取div的id标签属性值开头为a的div标签
        self.post.title = selector.xpath('//h1[@class="csdn_top"]/text()')
        print(Post.title)
        # try:
        #     file = open('/Users/vallzey/Downloads/test2', 'w', encoding='utf-8')
        #     file.write(data)
        # finally:
        #     file.close()


a = CsdnSpider()
a.save("https://blog.csdn.net/u011138533/article/details/72629728")