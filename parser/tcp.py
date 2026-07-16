from scapy.layers.inet import TCP
from util.protocol import Protocol

def parse(packet, info):
    if TCP not in packet:
        return

    tcp = packet[TCP]

    info.protocol = Protocol.TCP
    info.src_port = tcp.sport
    info.dst_port = tcp.dport
    info.flags = str(tcp.flags)
