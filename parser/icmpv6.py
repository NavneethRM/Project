from scapy.layers.inet6 import ICMPv6ND_NS, ICMPv6ND_NA, ICMPv6ND_RS, ICMPv6ND_RA
from util.protocol import ICMPv6, Protocol

def parse(packet, info):
    if ICMPv6ND_NS in packet:
        info.protocol = Protocol.ICMPv6
        info.icmpv6_type = ICMPv6.ICMPv6NS
    elif ICMPv6ND_RA in packet:
        info.protocol = Protocol.ICMPv6
        info.icmpv6_type = ICMPv6.ICMPv6RA
    elif ICMPv6ND_NA in packet:
        info.protocol = Protocol.ICMPv6
        info.icmpv6_type = ICMPv6.ICMPv6NA
    elif ICMPv6ND_RS in packet:
        info.protocol = Protocol.ICMPv6
        info.icmpv6_type = ICMPv6.ICMPv6RS
