from scapy.layers.inet6 import IPv6

def parse(packet, info):
    if IPv6 not in packet:
        return

    ipv6 = packet[IPv6]

    info.ipv6 = True
    info.src_ip = ipv6.src
    info.dst_ip = ipv6.dst
