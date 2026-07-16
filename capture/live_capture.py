from scapy.all import sniff

class liveCapture:
    def __init__(self, interface = None ):
        self.interface = interface

    def capture(self, packet_cout = 100):
        print(f"[*] Capturing {packet_cout} packets...")

        packet = sniff(iface = self.interface, count = packet_cout)
        print(f"[+] Captured {len(packet)} packets.")

        return packet
