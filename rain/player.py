import asyncio
import packet as pkt


class Player:
    def __init__(self, reader, writer) -> None:
        self.reader = reader
        self.writer = writer
        self.name = None
        self.verification_key = None

    async def recv(self):
        data = await self.reader.read(512)
        return data

    async def send(self, data):
        self.writer.write(data)
        await self.writer.drain()

    async def disconn(self):
        self.writer.close()
        await self.writer.wait_closed()

    async def ping(self):
        packet = pkt.Ping()
        while True:
            await asyncio.sleep(0.5)
            await self.send(packet.encode())


class PlayerHandler:
    def __init__(self, player) -> None:
        self.player = player

    async def start(self):
        await self.playeridentification()
        await self.serveridentification()

    async def playeridentification(self):
        data = await self.player.recv()
        packet = pkt.PlayerIdentification.decode(data)
        self.player.name = packet.username
        self.player.verification_key = packet.verification_key

    async def serveridentification(self):
        packet = pkt.ServerIdentification(b"Test", b"abc", 0x64)
        await self.player.send(packet.encode())
