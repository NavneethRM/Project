from core.flow import Flow

class FlowTable:
    def __init__(self):
        self.flows = {}

    def add_packet(self,packet):
        key = (
                packet.src_ip,
                packet.dst_ip,
                packet.src_port,
                packet.dst_port,
                packet.protocol,
                )

        if key not in self.flows:
            self.flows[key] = Flow(
                    packet.src_ip,
                    packet.dst_ip,
                    packet.src_port,
                    packet.dst_port,
                    packet.protocol,
                    )

        self.flows[key].add(packet)

    def __iter__(self):

        return iter(self.flows.values())


