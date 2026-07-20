import argparse

from capture.live_capture import liveCapture
from capture.offline_capture import OfflineCapture
from core.flow_table import FlowTable
from parser.parser import PacketParser
from detection.detector import DetectionEngine
from detection.syn_flood import SynFloodDetector
from detection.icmp_flood import ICMPFloodDetector
from detection.port_scan import PortScanDetector
from util.json_exporter import JSONExporter
from util.charts import ChartGenerator
from util.html_report import HTMLReport
from util.terminal import banner, show_alerts, show_summary, show_flows


def get_capture_source(args):
    if args.pcap:
        return OfflineCapture(args.pcap).packets()

    capture = liveCapture()
    return capture.capture(packet_count=args.count)


def main():

    com_parser = argparse.ArgumentParser(description="Lightweight Packet Analzyer")

    group = com_parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-p", "--pcap", help="Read packets from PCAP file.",)

    group.add_argument("-l", "--live", action="store_true", help="Capture live packets.")

    
    com_parser.add_argument("-c", "--count", type=int, default=100,help="Number of Packets to capture.")

    args = com_parser.parse_args()

    parser = PacketParser()
    table = FlowTable()

    packets = list(get_capture_source(args))

    engine = DetectionEngine()

    engine.register(SynFloodDetector())
    engine.register(ICMPFloodDetector())
    engine.register(PortScanDetector())

    exporter = JSONExporter()
    charts = ChartGenerator()
    report = HTMLReport()

    banner()

    for packet in packets:
        table.add_packet(parser.parse(packet))

    show_summary(len(packets), len(table))
    show_flows(table)

    all_alerts = []
    for flow in table:
        all_alerts.extend(engine.run(flow))
    show_alerts(all_alerts)

    # JSON 
    path = exporter.save(all_alerts)
    print(f"[+] Saved Report: {path}")
    # CHART
    chart_file = [charts.protocol_distribution(list(table)), charts.alert_distribution(list(all_alerts))]

    filename = report.generate(list(table), all_alerts, chart_file)

    print(f"[+] HTML Report generated: {filename}")
    
    print("=" * 80)


if __name__ == "__main__":
    main()
