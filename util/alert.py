from dataclasses import dataclass
from enum import Enum

class Severity(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3

@dataclass(slots=True)
class Alert:
    timestamp: float
    severity: Severity
    rule: str
    source_ip: str
    destination_ip: str
    description: str
