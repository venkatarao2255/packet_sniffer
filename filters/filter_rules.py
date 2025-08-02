from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.dns import DNS

def should_log_packet(packet):
    if IP in packet:
     
        return True  
    return False
