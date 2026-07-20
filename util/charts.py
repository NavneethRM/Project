from pathlib import Path
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self, output_dir="../output/charts"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)


    def protocol_distribution(self, flows):

        protocols = {}

        for flow in flows:

            if hasattr(flow.protocol, "name"):
                protocol = flow.protocol.name
            else:
                protocol = str(flow.protocol)

            protocols[protocol] = protocols.get(protocol, 0) + 1


        if not protocols:
            return None


        plt.figure(figsize=(8,5))

        plt.bar(
            list(protocols.keys()),
            list(protocols.values())
        )

        plt.xlabel("Protocol")
        plt.ylabel("Flows")
        plt.title("Protocol Distribution")

        path = self.output_dir / "protocol_distribution.png"

        plt.savefig(path, bbox_inches="tight")
        plt.close()

        return path



    def alert_distribution(self, alerts):

        severity_count = {}

        for alert in alerts:

            if hasattr(alert.severity, "name"):
                severity = alert.severity.name
            else:
                severity = str(alert.severity)


            severity_count[severity] = (
                severity_count.get(severity, 0) + 1
            )


        if not severity_count:
            return None


        plt.figure(figsize=(8,5))

        plt.bar(
            list(severity_count.keys()),
            list(severity_count.values())
        )

        plt.xlabel("Severity")
        plt.ylabel("Alerts")
        plt.title("Alert Severity Distribution")


        path = self.output_dir / "alert_severity.png"

        plt.savefig(path, bbox_inches="tight")
        plt.close()

        return path
