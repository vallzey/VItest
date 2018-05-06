# coding=utf-8
import urllib
import json


# 启动爬虫
# test_data = {'project': 'steam', 'spider': 'steampowered'}
# test_data_urlencode = urllib.parse.urlencode(test_data).encode('utf-8')
#
# requrl = "http://10.147.17.51:6800/listprojects.json"

# 以下是post请求
# req = urllib.request.Request(url = requrl, data = test_data_urlencode)
# req = urllib.request.Request(url = requrl)
# res_data = urllib.request.urlopen(req)
# res = res_data.read()  # res 是str类型
# jres = json.load(res_data.body)
# print(jres)
# 查看日志
# 以下是get请求
# myproject = "baidu"
# requrl = "http://localhost:6800/listjobs.json?project=" + myproject
# req = urllib.request.Request(requrl)
#
# res_data = urllib.request.urlopen(req)
# res = res_data.read()
# print(res)
baseUrl ='http://10.147.17.51:6800/'
daemUrl ='http://10.147.17.51:6800/daemonstatus.json'
listproUrl ='http://10.147.17.51:6800/listprojects.json'
listspdUrl ='http://10.147.17.51:6800/listspiders.json?project=%s'
listspdvUrl= 'http://10.147.17.51:6800/listversions.json?project=%s'
listjobUrl ='http://10.147.17.51:6800/listjobs.json?project=%s'
delspdvUrl= 'http://10.147.17.51:6800/delversion.json'
import requests
daemUrl = 'http://10.147.17.51:6800/daemonstatus.json'
listjobUrl ='http://10.147.17.51:6800/listjobs.json?project=steam'

r = requests.get(listproUrl)
print(r)
print(r.json())