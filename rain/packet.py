import struct
import enum
from dataclasses import dataclass, field


class PacketType(enum.IntEnum):
    CLIENT2SERVER = 0x00
    SERVER2CLIENT = 0x01


@dataclass
class PlayerIdentification:
    _packet_type = PacketType.CLIENT2SERVER

    packet_id: int
    protocol_version: int
    username: str
    verification_key: str
    unused: int

    @classmethod
    def decode(cls, data):
        unpacked_data = struct.unpack("BB64s64sB", data)
        return cls(*unpacked_data)


@dataclass
class ServerIdentification:
    _packet_type = PacketType.SERVER2CLIENT

    server_name: bytes
    server_motd: bytes
    user_type: int

    packet_id: int = field(default=0x00)
    protocol_version: int = field(default=0x07)

    def encode(self):
        packed_data = struct.pack(
            "BB64s64sB",
            self.packet_id,
            self.protocol_version,
            self.server_name,
            self.server_motd,
            self.user_type,
        )
        return packed_data


@dataclass
class Ping:
    _packet_type = PacketType.SERVER2CLIENT
    packet_id: int = field(default=0x01)

    def encode(self):
        packed_data = struct.pack("B", self.packet_id)
        return packed_data


@dataclass
class LevelInitialize:
    _packet_type = PacketType.SERVER2CLIENT
    packet_id: int = field(default=0x02)

    def encode(self):
        packed_data = struct.pack("B", self.packet_id)
        return packed_data
