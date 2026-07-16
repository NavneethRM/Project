from scapy.layers.l2 import Ether

def parse(packet, info):
    if Ether not in packet:
        return
    eth = packet[Ether]

    info.src_mac = eth.src
    info.dst_mac = eth.dst
