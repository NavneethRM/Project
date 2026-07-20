from detection.detector import Detector
from util.alert import Alert, Severity
from util.protocol import Protocol


class SynFloodDetector(Detector):

    SYN_THRESHOLD = 100

    def detect(self, flow):

        if flow.protocol != Protocol.TCP:
            return None

        if flow.syn_count < self.SYN_THRESHOLD:
            return None

        if flow.syn_count <= flow.ack_count:
            return None

        return Alert(
            timestamp=flow.end_time,
            source_ip=flow.endpoint_a[0],
            destination_ip=flow.endpoint_b[0],
            rule="SYN Flood",
            severity=Severity.CRITICAL,
            description=(
                f"SYN={flow.syn_count}, "
                f"ACK={flow.ack_count}, "
                f"Duration={flow.duration:.2f}s"
            ),
        )
