import os
import datetime
from scapy.layers.inet import IP, TCP, UDP, ICMP

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sniff_log.txt")
os.makedirs(LOG_DIR, exist_ok=True)

def log_packet(packet):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    proto = "UNKNOWN"
    src = dst = sport = dport = "-"

    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

    if TCP in packet:
        proto = "TCP"
        sport = packet[TCP].sport
        dport = packet[TCP].dport
    elif UDP in packet:
        proto = "UDP"
        sport = packet[UDP].sport
        dport = packet[UDP].dport
    elif ICMP in packet:
        proto = "ICMP"


    log_line = f"[{timestamp}] {proto} | {src}:{sport} -> {dst}:{dport}"


    print(log_line)

 
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")
