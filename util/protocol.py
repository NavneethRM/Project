from enum import Enum

class ICMPv6(Enum):
    ICMPv6NS = "Neighbour Solicitation"
    ICMPv6NA = "Neighbour Advertisement"
    ICMPv6RS = "Router Solicitation"
    ICMPv6RA = "Router Advertisement"

class Protocol(Enum):
    UNKNOWN = 0
    ARP = 1
    ICMP = 2
    ICMPv6 = 3
    TCP = 4
    UDP = 5
