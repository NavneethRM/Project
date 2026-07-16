from dataclasses import dataclass, field
from collections import Counter
from util.packet_model import PacketInfo
from util.protocol import Protocol

@dataclass(slots=True)
class Flow:

    endpoint_a: tuple[str, int | None]
    endpoint_b: tuple[str, int | None]

    protocol: Protocol

    packet_count: int = 0
    byte_count: int = 0

    syn_count: int = 0
    ack_count: int = 0
    fin_count: int = 0
    rst_count: int = 0

    start_time: float = 0
    end_time: float = 0

    applications: Counter = field(default_factory=Counter)
    
    def add(self, packet: PacketInfo) -> None:
        if self.packet_count == 0:
            self.start_time = packet.timestamp

        self.end_time = packet.timestamp

        self.packet_count += 1
        self.byte_count += packet.length

        if packet.application:
            self.applications[packet.application] += 1

        if packet.flags:
            flags = str(packet.flags)

            if "S" in flags:
                self.syn_count += 1
            if "A" in flags:
                self.ack_count += 1
            if "F" in flags:
                self.fin_count += 1
            if "R" in flags:
                self.rst_count += 1

    @property
    def duration(self):
    
        return max(self.end_time - self.start_time, 0.0)

    @property
    def packets_per_second(self):
        if self.duration == 0.0:
            return float(self.packet_count)
        return self.packet_count / self.duration

    @property
    def bytes_per_second(self):
        if self.duration == 0.0:
            return float(self.byte_count)
        return self.byte_count / self.duration

    def __str__(self):
        return (
            f"{self.protocol.name} "
            f"{self.endpoint_a[0]}:{self.endpoint_a[1]} "
            f"<-> "
            f"{self.endpoint_b[0]}:{self.endpoint_b[1]}\n"
            f"Packets : {self.packet_count}\n"
            f"Bytes   : {self.byte_count}\n"
            f"SYN     : {self.syn_count}\n"
            f"ACK     : {self.ack_count}\n"
            f"FIN     : {self.fin_count}\n"
            f"RST     : {self.rst_count}\n"
            f"Duration: {self.duration:.3f}s"
        )


def flow_key(packet: PacketInfo):
    ep1 = (packet.src_ip or "", packet.src_port if packet.src_port is not None else -1)
    ep2 = (packet.dst_ip or "", packet.dst_port if packet.dst_port is not None else -1)

    if ep1 <= ep2:
        
        return ep1, ep2, packet.protocol
    return ep2, ep1, packet.protocol
