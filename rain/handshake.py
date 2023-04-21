import asyncio
from world import WorldHandler
from player import PlayerHandler


class Handshake:
    def __init__(self, world, player) -> None:
        self.player = player
        self.plrhndlr = PlayerHandler(player)
        self.wrldhndlr = WorldHandler(world, player)

    async def execute(self):
        await self.plrhndlr.start()
        self.loop()
        await self.wrldhndlr.start()

    def loop(self):
        asyncio.create_task(self.player.ping())
