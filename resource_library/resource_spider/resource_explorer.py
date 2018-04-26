import urllib.request
import ssl
from lxml import etree
from resource_library.models import Post, Category, Tag, Author, Origin
import resource_library.resource_spider.origin as ogn


class ResourceExplorer(object):
    def __init__(self, url=None, origin=None, method=None):
        self.url = url
        self.origin = origin
        self.method = method or "simple"
        self.post = Post()
        self.author = Author()

    def get_content(self):
        if self.url is None:
            print("url can't be None")
            return
        if self.origin is None:
            print("origin can't be None")
            return
        getter = ogn.get_csdn_exploer()
        data = getter.get_content(url=self.url)
        saver = ogn.get_csdn_saver()
        self.post = saver.save_from_html(data)
        self.post.url = self.url
        self.post.save()

