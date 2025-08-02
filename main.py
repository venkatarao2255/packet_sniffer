from scapy.all import sniff, get_if_list, IP, TCP, UDP, ICMP
from utils.logger import log_packet


INTERFACE = "Wi-Fi"  

def packet_callback(packet):
    if IP in packet:
        log_packet(packet)
        print(packet.summary())

print(f"[*] Starting packet sniffer on interface: {INTERFACE}")
sniff(iface=INTERFACE, prn=packet_callback, store=False)
