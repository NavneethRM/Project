from pathlib import Path
from datetime import datetime


class HTMLReport:

    def __init__(self, output="output"):
        self.output = Path(output)
        self.output.mkdir(exist_ok=True)


    def generate(self, flows, alerts, charts):

        filename = (
            self.output /
            f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        )


        with open(filename, "w") as f:

            f.write("""
<html>
<head>

<title>Network Analysis Report</title>

<style>

body {
    font-family: Arial;
    margin:40px;
}

table {
    border-collapse: collapse;
    width:100%;
}

td,th {
    border:1px solid #ddd;
    padding:8px;
}

th {
    background:#333;
    color:white;
}

.alert {
    color:red;
}

</style>

</head>

<body>

<h1>Network Analysis Report</h1>

""")


            f.write(
                f"<p>Generated: {datetime.now()}</p>"
            )


            f.write(
                f"<h2>Flows: {len(flows)}</h2>"
            )


            f.write("""
<table>
<tr>
<th>Protocol</th>
<th>Source</th>
<th>Destination</th>
<th>Packets</th>
<th>Bytes</th>
</tr>
""")


            for flow in flows:

                f.write(
                f"""
<tr>
<td>{flow.protocol.name}</td>
<td>{flow.endpoint_a}</td>
<td>{flow.endpoint_b}</td>
<td>{flow.packet_count}</td>
<td>{flow.byte_count}</td>
</tr>
"""
                )


            f.write("</table>")


            f.write(
                f"<h2>Alerts: {len(alerts)}</h2>"
            )


            if alerts:

                f.write("""
<table>
<tr>
<th>Rule</th>
<th>Severity</th>
<th>Source</th>
<th>Destination</th>
</tr>
""")

                for alert in alerts:

                    f.write(
                    f"""
<tr>
<td>{alert.rule}</td>
<td>{alert.severity.name}</td>
<td>{alert.source_ip}</td>
<td>{alert.destination_ip}</td>
</tr>
"""
                    )

                f.write("</table>")

            else:
                f.write("<p>No alerts detected.</p>")


            for chart in charts:

                if chart:
                    f.write(
                    f"""
<h2>Chart</h2>
<img src="{chart}" width="600">
"""
                    )


            f.write("""
</body>
</html>
""")


        return filename
