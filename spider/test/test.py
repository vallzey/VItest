import spider.scrapyd as spsd

http = spsd.get_http()
data = http.request(url='http://10.147.17.51:6800/listprojects.json')
print(data['node_name'])

sd_req = spsd.get_scrapyd_request(server='10.147.17.51')
data = sd_req.project_list()
print(data['projects'])