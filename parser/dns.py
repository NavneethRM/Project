from scapy.layers.dns import DNS

def parse(packet, info):
    if DNS in packet:
        info.application = "DNS"
