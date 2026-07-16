from dataclasses import dataclass
from collections import Counter
from core.packet_model import PacketInfo

@dataclass(slots=True)
class Flow:
    src_ip: str
    dast_ip: str

    src_port: int | None
    dst_port: int | None

    protocol: str
    packets: list[PacketInfo] = field(default_factory=list)
    bytes: int = 0

    def add(self, packet:PacketInfo):
        self.packets.append(packet)
        self.bytes += packet.length

    @property
    def packet_count(self):
        
        return len(self.packets)
