from detection.detector import Detector
from util.alert import Alert, Severity
from util.protocol import Protocol


class ICMPFloodDetector(Detector):

    PACKETS_PER_SECOND = 50

    def detect(self, flow):

        if flow.protocol not in (Protocol.ICMP, Protocol.ICMPv6):
            return None

        if flow.packets_per_second < self.PACKETS_PER_SECOND:
            return None

        return Alert(
            timestamp=flow.end_time,
            source_ip=flow.endpoint_a[0],
            destination_ip=flow.endpoint_b[0],
            rule="ICMP Flood",
            severity=Severity.HIGH,
            description=f"{flow.packets_per_second:.1f} packets/sec",
        )
