import logging

import requests

'''
:param request_type: get/post
:param url:
:param data:
:param retry_times:
:param return_type: text/json
:return:
'''


class Http(object):
    def __init__(self, retry_times=None):
        self.retry_times = retry_times or 5
        self.url = None

    def request_get(self, url, retry_times=5):
        '''
        :param url:
        :param retry_times:
        :return: response obj
        '''
        for i in range(retry_times):
            try:
                res = requests.get(self.url)
            except Exception as e:
                logging.warning('request error retry %s' % url)
                continue
            return res

    def request_post(self, data, retry_times=5):
        '''
        :param url:
        :param retry_times:
        :return: response obj
        '''
        for i in range(retry_times):
            try:
                res = requests.post(self.url, data)
            except Exception as e:
                logging.warning('request error retry %s' % self.url)
                continue
            return res

    def request(self, url=None, request_type='get', data=None, return_type='json'):
        if url is None:
            logging.warning('url can not be None');
        self.url = url
        if request_type == 'get':
            res = self.request_get(self.retry_times)
        if request_type == 'post':
            res = self.request_post(data, self.retry_times)
        if not res: return res
        if return_type == 'text':
            return res.text
        if return_type == 'json':
            try:
                res = res.json()
                return res
            except Exception as e:
                logging.warning('parse json error %s' % str(e))
                return None
