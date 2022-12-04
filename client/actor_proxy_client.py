from dapr.actor import ActorProxy, ActorId
from spider_sdk.interface.cookie_actor_interface import CookieActorInterface
from spider_sdk.interface.proxy_actor_interface import ProxyActorInterface
from spider_sdk.interface.spider_setting_actor_interface import SpiderSettingActorInterface
from spider_sdk.interface.breeder_actor_interface import BreederActorInterface

"""
    通用的边车服务代理类
"""


class ActorProxyClient:

    def __init__(self, actor_id):
        self._actor_id = actor_id

    @property
    def actor_id(self):
        return self._actor_id

    def cookie_actor_proxy(self):
        return ActorProxy.create('CookieActor', ActorId(self.actor_id), CookieActorInterface)

    def proxy_actor_proxy(self):
        return ActorProxy.create('ProxyActor', ActorId(self.actor_id), ProxyActorInterface)

    def spider_setting_actor_proxy(self):
        return ActorProxy.create('SpiderSettingActor', ActorId(self.actor_id), SpiderSettingActorInterface)

    def breeder_actor_proxy(self):
        return ActorProxy.create('BreederActor', ActorId(self.actor_id), BreederActorInterface)

