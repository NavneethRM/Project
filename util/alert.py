from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass(slots=True)
class Alert:
    timestamp: float

    source_ip: str
    destination_ip: str

    rule: str
    severity: Severity

    description: str

    def __str__(self):
        return (
            f"[{self.severity.value}] "
            f"{self.rule}\n"
            f"Source      : {self.source_ip}\n"
            f"Destination : {self.destination_ip}\n"
            f"Time        : {self.timestamp:.3f}\n"
            f"{self.description}"
        )
