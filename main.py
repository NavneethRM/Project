from capture.live_capture import liveCapture
from core.flow_table import FlowTable
from parser.parser import PacketParser

def main():
    capture = liveCapture()
    parser = PacketParser()

    packets = capture.capture(packet_cout=10)

    table = FlowTable()

    print("\nParsed Packets")
    print("-" * 80)

    for packet in packets:
        info = parser.parse(packet)
        table.add_packet(info)
    print()

    for flow in table:
        print(flow)




if __name__ == "__main__":
    main()
