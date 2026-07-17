from scapy.all import PcapReader


class OfflineCapture:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def packets(self):
        print(f"[*] Reading PCAP: {self.filename}")

        count = 0

        with PcapReader(self.filename) as reader:
            for packet in reader:
                count += 1
                yield packet

        print("[+] Finished reading {count} packets.")
