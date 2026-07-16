from scapy.layers.inet import UDP
from core.protocol import Protocol

def parse(packet, info):
    if UDP not in packet:
        return

    udp = packet[UDP]

    info.protocol = Protocol.UDP 
    info.src_port = udp.sport
    info.dst_port = udp.dport
