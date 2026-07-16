from capture.live_capture import liveCapture
from core.flow_table import FlowTable
from parser.parser import PacketParser

def main():
    capture = liveCapture()
    parser = PacketParser()

    packets = capture.capture(packet_cout=100)

    table = FlowTable()

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
