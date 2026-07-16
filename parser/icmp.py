from scapy.layers.inet import ICMP
from util.protocol import Protocol

def parse(packet, info):
    if ICMP not in packet:
        return
    info.protocol = Protocol.ICMP
