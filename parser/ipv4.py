from scapy.layers.inet import IP

def parse(packet, info):
    if IP not in packet:
        return

    ip = packet[IP]
    info.src_ip = ip.src
    info.dst_ip = ip.dst
