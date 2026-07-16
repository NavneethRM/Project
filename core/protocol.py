from enum import Enum

class Protocol(Enum):
    UNKNOWN = 0
    ARP = 1
    ICMP = 2
    TCP = 3
    UDP = 4
