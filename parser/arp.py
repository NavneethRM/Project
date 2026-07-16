from scapy.layers.l2 import ARP
from core.protocol import Protocol

def parse(packet, info):
    if ARP not in packet:
        return

    arp = packet[ARP]

    info.protocol = Protocol.ARP
    info.src_ip = arp.psrc
    info.dst_ip = arp.pdst
