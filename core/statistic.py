class Statistic:

    def __init__(self, flows):
        self.flows = flows

    def total_packets(self):
        return sum(flow.packet_count for flow in self.flows)

    def total_bytes(self):
        return sum(flow.byte_count for flow in self.flows)
