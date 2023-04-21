import asyncio

from player import Player
from handshake import Handshake
from world import World


class Server:
    def __init__(self) -> None:
        self.players = []
        self.world = World()

    async def create_player(self, reader, writer):
        player = Player(reader, writer)
        handshake = Handshake(self.world, player)
        self.players.append(player)

        await handshake.execute()

    async def run(self):
        server = await asyncio.start_server(self.create_player, "127.0.0.1", 25565)
        async with server:
            await server.serve_forever()


server = Server()
asyncio.run(server.run())
