from util.protocol import  ICMPv6, Protocol
from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)

class PacketInfo:
    timestamp: float

    src_mac: Optional[str] = None
    dst_mac: Optional[str] = None
    src_ip: Optional[str] = None
    dst_ip: Optional[str] = None

    src_port: Optional[int] = None
    dst_port: Optional[int] = None

    ipv4: bool = False
    ipv6: bool = False

    protocol: Protocol = Protocol.UNKNOWN
    icmpv6_type: Optional[ICMPv6] = None

    flags: Optional[str] = None

    length: int = 0

    application: Optional[str] = None
