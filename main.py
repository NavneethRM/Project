import argparse

from capture.live_capture import liveCapture
from capture.offline_capture import OfflineCapture
from core.flow_table import FlowTable
from parser.parser import PacketParser


def get_capture_source(args):
    if args.pcap:
        return OfflineCapture(args.pcap).packets()

    capture = liveCapture()
    return capture.capture(packet_cout=args.count)


def main():

    com_parser = argparse.ArgumentParser(description="Lightweight Packet Analzyer")

    group = com_parser.add_mutually_exclusive_group()

    group.add_argument("-p", "--pcap", help="Read packets from PCAP file.",)

    group.add_argument("-l", "--live", action="store_true", help="Capture live packets.")

    
    com_parser.add_argument("-c", "--count", type=int, default=100,help="Number of Packets to capture.")

    args = com_parser.parse_args()

    parser = PacketParser()
    table = FlowTable()

    packets = get_capture_source(args)

    print("\nParsed Packets")
    print("-" * 80)

    for packet in packets:
        table.add_packet(parser.parse(packet))
    print(f"\nFlows: {len(table)}\n")

    for flow in table:
        print(flow)
        print("-" * 80)


if __name__ == "__main__":
    main()
