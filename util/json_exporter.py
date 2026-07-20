import json
from pathlib import Path
from enum import Enum
from datetime import datetime

import json
from pathlib import Path
from datetime import datetime
from enum import Enum


class JSONExporter:

    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)


    def save(self, alerts, filename=None):

        self.output_dir.mkdir( parents=True, exist_ok=True)

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = (self.output_dir / f"alerts_{timestamp}.json")

        else:
            filename = Path(filename)

        data = []

        for alert in alerts:

            severity = alert.severity

            if isinstance(severity, Enum):
                severity = severity.value


            data.append({
                "timestamp": alert.timestamp,
                "source": alert.source_ip,
                "destination": alert.destination_ip,
                "rule": alert.rule,
                "severity": severity,
                "description": alert.description,
            })


        with open( filename, "w", encoding="utf-8" ) as f:
            json.dump( data, f, indent=4)

        return filename
