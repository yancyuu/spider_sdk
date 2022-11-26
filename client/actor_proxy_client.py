import os

from dapr.actor import ActorProxy, ActorId
from spider_sdk.interface.cookie_actor_interface import CookieActorInterface
from spider_sdk.interface.proxy_actor_interface import ProxyActorInterface
from spider_sdk.interface.spider_setting_actor_interface import SpiderSettingActorInterface
from spider_sdk.interface.fixed_rules_spider_actor_interface import FixedRulesSpiderActorInterface

"""
    通用的边车服务代理类
"""


class ActorProxyClient:

    def __init__(self, actor_id):
        self._actor_id = actor_id

    @property
    def actor_id(self):
        return self._actor_id

    def create_cookie_actor_proxy(self):
        return ActorProxy.create('CookieActor', ActorId(self.actor_id), CookieActorInterface)

    def create_proxy_actor_proxy(self):
        return ActorProxy.create('ProxyActor', ActorId(self.actor_id), ProxyActorInterface)

    def create_spider_setting_actor_proxy(self):
        return ActorProxy.create('SpiderSettingActor', ActorId(self.actor_id), SpiderSettingActorInterface)

    def create_fixed_rules_spider_actor_proxy(self):
        return ActorProxy.create('FixedRulesSpiderActor', ActorId(self.actor_id), FixedRulesSpiderActorInterface)

