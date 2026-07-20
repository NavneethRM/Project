from scapy.all import sniff

class liveCapture:
    def __init__(self, interface = None ):
        self.interface = interface

    def capture(self, packet_count = 100):
        print(f"[*] Capturing {packet_count} packets...")

        packet = sniff(iface = self.interface, count = packet_count)
        print(f"[+] Captured {len(packet)} packets.")

        return packet
