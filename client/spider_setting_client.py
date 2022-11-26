# -*- coding: utf-8 -*-
from spider_sdk.client.actor_proxy_client import ActorProxyClient
from spider_sdk.client.http_client import HttpClient

'''
供前台服务调用的通用方法
'''


class SpiderSettingClient(HttpClient):

    def __init__(self, builder, id):
        super().__init__(builder)
        self.actor_proxy = ActorProxyClient(id)
        self.spider_setting = self.actor_proxy.create_spider_setting_actor_proxy()

    def get_search(self):
        return self.make_get_request_by_setting()

