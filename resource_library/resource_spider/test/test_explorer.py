import resource_library.resource_spider as rsp

explorer = rsp.explorer(url='https://blog.csdn.net/u013510614/article/details/50187515', origin='csdn')
explorer.get_content()