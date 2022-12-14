from spider_sdk.client.actor_proxy_client import ActorProxyClient
from common_sdk.system.sys_env import get_env
from faker import Faker
from spider_sdk.builder.base_builder import BaseBuilder

"""
    用于处理请求时的内容封装(根据配置和特殊页面封装)
"""


class BreederBuilder(BaseBuilder):
    def __init__(self):
        super().__init__(
            headers={
                "content-type": "text/html; charset=utf-8"
            })
        self.proxy = None
        self.actor_proxy = ActorProxyClient(BreederBuilder.__name__)

    # 根据配置查询页面
    async def make_get_request_by_setting(self):
        if get_env("USE_COOKIE_POOL"):
            actor_proxy = self.actor_proxy.cookie_actor_proxy()
            cookie = await actor_proxy.getCookie()
            # 在builder中增加cookie
            if cookie:
                self.headers.update({"cookie": cookie.get("cookie")})
        if get_env("RANDOM_AGENT"):
            # 在builder中增加随机agent
            faker_handel = Faker()
            self.header.update({"agent": faker_handel.user_agent()})
        if get_env("USE_PROXY"):
            actor_proxy = self.actor_proxy.create_proxy_actor_proxy()
            proxy = await actor_proxy.getProxy()
            self.proxy = proxy
