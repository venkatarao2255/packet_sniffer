# Packet Sniffer

A simple packet sniffer built using Python and the `socket` module. This tool captures network packets in real-time and prints key information from their headers, such as IP addresses, protocols, ports, and more. The sniffer also supports basic filtering and logs packets to a file.

## Features

- Captures raw network packets using raw sockets
- Displays:
  - Ethernet Frame Details
  - IPv4 Header Information
  - TCP/UDP Header Data
  - ICMP Packet Info
- Lists available network interfaces
- Allows custom filter rules (via `filter_rules.py`)
- Logs packet data to `logs/sniff_log.txt`
- Structured modular codebase

## Learning Goals

This project was built to gain hands-on experience with:

- Core networking concepts and the TCP/IP protocol stack
- Low-level network programming using raw sockets in Python
- The structure of Ethernet, IP, TCP, UDP, and ICMP headers
- The OSI model in real-world packet traversal
- Binary parsing techniques and data formatting
- How tools like firewalls, packet analyzers, and IDS work under the hood

By manually inspecting and processing network packets, this tool offers a deeper understanding of how data moves across a network and what it looks like at every layer.

## How It Works

The program opens a raw socket on the selected interface and continuously reads packets. Each packet is parsed step-by-step, extracting relevant data and applying any custom-defined filters. Matching packets are both printed to the console and saved to the log file.

## File Structure

```
packet_sniffer/
│
├── .github/                # GitHub-specific workflows (if any)
├── filters/
│   └── filter_rules.py     # Define packet filter logic (e.g., IPs, protocols)
│
├── logs/
│   └── sniff_log.txt       # Output log for captured packets
│
├── utils/
│   └── list_interfaces.py  # Lists available network interfaces
│
├── main.py                 # Entry point: captures and processes packets
├── __pycache__/            # Python bytecode cache (ignored in version control)
```

## Requirements

- Python 3.6+
- OS: Linux or macOS (Windows not supported for raw sockets)
- Root/Admin privileges to run with raw socket access

## Usage

1. Clone the repository:

```bash
git clone https://github.com/venkatarao2255/packet_sniffer.git
cd packet_sniffer
```

2. List available network interfaces (optional):

```bash
python3 utils/list_interfaces.py
```

3. Run the packet sniffer:

```bash
sudo python3 main.py
```

> **Note**: `sudo` is required to create raw sockets and access low-level network interfaces.

## Logging

All captured packet summaries are saved to:

```
logs/sniff_log.txt
```

This log file will grow as packets are captured. You can redirect it, rotate it, or parse it for analysis.

## Filtering

You can define your own filtering logic inside `filters/filter_rules.py`. For example, you might choose to:

- Ignore packets from certain IPs
- Capture only TCP packets
- Log only packets with specific destination ports

Modify `filter_rules.py` to suit your use case.

## Next Steps (Ideas for Extension)

If you're interested in continuing this learning journey, here are a few suggestions:

- Reconstruct full TCP streams (packet reassembly)
- Add support for IPv6 packets
- Build a GUI dashboard with live packet visualization
- Use the `scapy` or `dpkt` library for advanced decoding
- Create Wireshark-compatible `.pcap` output
- Add real-time packet filtering via command-line arguments
- Integrate with a web server to expose packet logs via a REST API

## Author

**Venkatarao Dasari**  
[GitHub Profile](https://github.com/venkatarao2255)
