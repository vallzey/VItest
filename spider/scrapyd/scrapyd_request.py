import requests
import spider.scrapyd as spsd
'''
baseUrl ='http://10.147.17.51:6800/'
daemUrl ='http://10.147.17.51:6800/daemonstatus.json'
listproUrl ='http://10.147.17.51:6800/listprojects.json'
listspdUrl ='http://10.147.17.51:6800/listspiders.json?project=%s'
listspdvUrl= 'http://10.147.17.51:6800/listversions.json?project=%s'
listjobUrl ='http://10.147.17.51:6800/listjobs.json?project=%s'
delspdvUrl= 'http://10.147.17.51:6800/delversion.json'
'''



class Requests(object):
    def __init__(self, server=None, port=None):
        self.server = server or '127.0.0.1'
        self.port = port or '6800'
        self.base_url = None
        if self.server is None:
            return
        self.http = spsd.get_http()

        self.base_url = 'http://'+self.server+':'+self.port+'/'
        self.list_projects = self.base_url+'listprojects.json'

    def project_list(self):
        if self.server is None:
            return
        data = self.http.request(url=self.list_projects)
        return data
