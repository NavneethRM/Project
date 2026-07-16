from core.flow import Flow, flow_key

class FlowTable:
    def __init__(self):
        self.flows: dict = {}

    def add_packet(self, packet):
        key = flow_key(packet)

        if key not in self.flows:
            endpoint_a, endpoint_b, protocol = key

            self.flows[key] = Flow(
                    endpoint_a=endpoint_a,
                    endpoint_b=endpoint_b,
                    protocol=protocol,
                    )

        self.flows[key].add(packet)

    def __iter__(self):
        return iter(self.flows.values())

    def __len__(self):
        return len(self.flows)

