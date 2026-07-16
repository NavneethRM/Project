from enum import Enum

class Protocol(Enum):
    UNKNOWN = 0
    ARP = 1
    ICMP = 2
    ICMPv6 = 3
    TCP = 4
    UDP = 5
