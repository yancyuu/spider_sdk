# -*- coding: utf-8 -*-
from common_sdk.logging.logger import logger
from urllib.parse import urlencode

import httpx

"""
    通用的http处理类
"""


class HttpClient(object):
    def __init__(self):
        self.client = httpx.AsyncClient()

    """
        post请求关注返回值
    """

    async def make_post_request(self, url, proxy=None, param=None, headers=None):
        url = 'http://{}/'.format(url)
        try:
            if proxy:
                logger.info("发送POST请求---->url{}   proxy---->{}".format(url, proxy))
                # todo: 代理
                self.client.proxies = httpx.Proxy(
                    url=proxy,
                )
                res = await self.client.post(url, json=param, headers=headers)
            else:
                logger.info("发送POST请求---->url{}".format(url))
                res = await self.client.post(url, json=param, headers=headers)
            if res:
                return res
            else:
                return {}
        except Exception as e:
            logger.info("请求失败{}".format(e))
            return False

    '''
        get请求关注返回的content（做解析）
    '''

    async def make_get_request(self, url, proxy=None, param=None, headers=None):
        url = 'http://{}'.format(url)
        if param:
            url += "?" + urlencode(param)
        try:
            if proxy:
                self.client.proxies = httpx.Proxy(
                    url=proxy,
                )
                logger.info("发送GET请求---->url{}   proxy---->{}".format(url, proxy))
                res = await self.client.get(url, headers=headers)
            else:
                logger.info("发送GET请求---->url{}".format(url))
                res = await self.client.get(url, headers=headers)
            if res:
                return res
            else:
                return ""
        except Exception as e:
            logger.info("请求失败{}".format(e))
            return False
