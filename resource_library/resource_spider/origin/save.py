from lxml import etree
from resource_library.models import Post, Category, Tag, Author, Origin


class CommonSave(object):
    def __init__(self):
        post = Post()
        author = Author()

    def save_from_csdn(self, data):
        selector = etree.HTML(data)
        # 使用starts - with方法提取div的id标签属性值开头为a的div标签
        self.post.title = selector.xpath('//h1[@class="csdn_top"]/text()')
        print(self.post.title)
        # try:
        #     file = open('/Users/vallzey/Downloads/test2', 'w', encoding='utf-8')
        #     file.write(data)
        # finally:
        #     file.close()
