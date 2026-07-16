from scapy.all import rdpcap


class pcapReader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        print(f"[*] Loading {self.filename}")
        packet = rdpcap(self.filename)
        print(f"[+] Loaded {len(packet)} packets")

        return packet
