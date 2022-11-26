# -*- coding: utf-8 -*-
from spider_sdk.client.actor_proxy_client import ActorProxyClient
from spider_sdk.client.http_client import HttpClient

'''
供前台服务调用的通用方法
'''


class SpiderClient(HttpClient):

    def __init__(self, builder, id):
        super().__init__(builder, id)
        self.actor_proxy = ActorProxyClient(id)
        self.spider = self.actor_proxy.create_spider_actor_proxy()

    def get_search(self):
        return self.make_get_request()

