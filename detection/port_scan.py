from collections import defaultdict

from detection.detector import Detector
from util.alert import Alert, Severity


class PortScanDetector(Detector):

    MEDIUM_THRESHOLD = 15
    HIGH_THRESHOLD = 50

    def __init__(self):

        self.ports = defaultdict(set)

    def detect(self, flow):

        src = flow.endpoint_a[0]
        dst_port = flow.endpoint_b[1]

        if dst_port < 0:
            return None

        self.ports[src].add(dst_port)

        count = len(self.ports[src])

        if count >= self.HIGH_THRESHOLD:

            return Alert(
                timestamp=flow.end_time,
                source_ip=src,
                destination_ip=flow.endpoint_b[0],
                rule="Port Scan",
                severity=Severity.HIGH,
                description=f"{count} unique destination ports",
            )

        if count >= self.MEDIUM_THRESHOLD:

            return Alert(
                timestamp=flow.end_time,
                source_ip=src,
                destination_ip=flow.endpoint_b[0],
                rule="Port Scan",
                severity=Severity.MEDIUM,
                description=f"{count} unique destination ports",
            )

        return None
