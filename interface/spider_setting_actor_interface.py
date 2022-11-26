from dapr.actor import ActorInterface, actormethod


class SpiderSettingActorInterface(ActorInterface):
    @actormethod(name="GenerateParseSettings")
    async def generate_parse_settings(self, data: dict) -> object:
        ...

    @actormethod(name="DeleteParseSettings")
    async def delete_parse_settings(self, data: dict) -> object:
        ...

    @actormethod(name="StartCrawling")
    async def start_crawling(self) -> object:
        ...

    @actormethod(name="GetMyData")
    async def get_my_data(self) -> object:
        ...

    @actormethod(name="SetMyData")
    async def set_my_data(self, data: object) -> None:
        ...

    @actormethod(name="ClearMyData")
    async def clear_my_data(self) -> None:
        ...

    @actormethod(name="SetReminder")
    async def set_reminder(self, enabled: bool) -> None:
        ...

    @actormethod(name="SetTimer")
    async def set_timer(self, enabled: bool) -> None:
        ...

    @actormethod(name="GetReentrancyStatus")
    async def get_reentrancy_status(self) -> bool:
        ...