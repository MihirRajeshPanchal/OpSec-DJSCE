from scapy.all import sniff, Packet, TCP, IP

def packet_callback(packet):
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        src_port = packet[TCP].sport
        dst_ip = packet[IP].dst
        dst_port = packet[TCP].dport
        data = str(packet[TCP].payload)
        
        print(f"Packet from {src_ip}:{src_port} to {dst_ip}:{dst_port}")
        print(f"Data: {data}")

if __name__ == '__main__':
    print("Monitoring network traffic on Windows...")
    
    interface = 'Ethernet'
    
    sniff(filter="tcp", prn=packet_callback, iface=interface)
