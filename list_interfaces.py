from scapy.all import get_if_list

print("Available interfaces:")
for iface in get_if_list():
    print("-", iface)
