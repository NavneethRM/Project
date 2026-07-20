from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def banner():
    console.print(Panel("[bold cyan]Lightweight Packet Analzyer[/bold cyan]", expand=False))

def show_summary(packet_count, flow_count):
    table = Table(title="Analysis Summary")
    table.add_column("Metric")
    table.add_column("Value")
    table.add_row("Packets", str(packet_count))
    table.add_row("Flows", str(flow_count))

    console.print(table)

def show_flows(flows):

    table = Table(
        title="Network Flows"
    )

    table.add_column("Protocol")
    table.add_column("Source")
    table.add_column("Destination")
    table.add_column("Packets")
    table.add_column("Bytes")


    for flow in flows:

        table.add_row(
            str(flow.protocol.name),
            str(flow.endpoint_a),
            str(flow.endpoint_b),
            str(flow.packet_count),
            str(flow.byte_count)
        )


    console.print(table)

def show_alerts(alerts):

    if not alerts:
        console.print(
            "[green]No threats detected[/green]"
        )
        return

    table = Table(title="Detected Alerts")

    table.add_column("Rule")
    table.add_column("Severity")
    table.add_column("Source")
    table.add_column("Destination")

    for alert in alerts:
        table.add_row(
            alert.rule,
            str(alert.severity.name),
            alert.source_ip,
            alert.destination_ip
        )

    console.print(table)

