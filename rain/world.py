import packet as pkt


class World:
    def __init__(self) -> None:
        pass


class WorldHandler:
    def __init__(self, world, player) -> None:
        self.player = player
        self.world = world

    async def start(self):
        await self.levelinitialize()

    async def levelinitialize(self):
        packet = pkt.LevelInitialize()
        await self.player.send(packet.encode())
