from core.packet_model import PacketInfo

from parser import enthernet, arp, ipv4, icmp, dns, udp ,tcp

class PacketParser:
    def parse(self, packet):

        info = PacketInfo(timestamp=float(packet.time), length=len(packet),)

        enthernet.parse(packet, info)
        arp.parse(packet, info)
        ipv4.parse(packet, info)
        tcp.parse(packet, info)
        udp.parse(packet, info)
        icmp.parse(packet, info)
        dns.parse(packet, info)

        return info
