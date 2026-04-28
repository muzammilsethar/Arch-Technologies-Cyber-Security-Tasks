Python
import scapy.all as scapy

def sniff(interface):
    # Capturing packets on the specified interface
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    # Extracting and printing packet details
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        print(f"[+] Source: {ip_src} --> Destination: {ip_dst} | Protocol: {protocol}")

# Starting the sniffer
sniff("any")
