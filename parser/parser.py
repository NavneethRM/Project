from util.packet_model import PacketInfo
from parser import ethernet, arp, icmpv6, ipv4, icmp, dns, ipv6, udp ,tcp

class PacketParser:
    def parse(self, packet):

        info = PacketInfo(timestamp=float(packet.time), length=len(packet),)

        ethernet.parse(packet, info)

        arp.parse(packet, info)
        ipv4.parse(packet, info)
        ipv6.parse(packet, info)

        tcp.parse(packet, info)
        udp.parse(packet, info)
        icmp.parse(packet, info)
        icmpv6.parse(packet,info)

        dns.parse(packet, info)

        return info
