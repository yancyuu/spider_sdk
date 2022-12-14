# -*- coding: utf-8 -*-
from spider_sdk.client.actor_proxy_client import ActorProxyClient
from spider_sdk.client.http_client import HttpClient

'''
供前台服务调用的通用方法
'''


class BreederClient(HttpClient):

    async def get(self, builder):
        await builder.make_get_request_by_setting()
        return await self.make_get_request(url=builder.url, headers=builder.header, proxy=builder.proxy, param=builder.param)
