#!/usr/bin/env python3

from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP, DNS, Raw
from datetime import datetime

def packet_callback(packet):

	timestamp = datetime.now().strftime("%H:%M:%S")

	print("\n" + "=" * 70)
	print(f"Time: {timestamp}")

	#ARP Packet
	if packet.haslayer(ARP):

		arp = packet[ARP]

		print("Protocol: ARP")
		print(f"Source MAC:  {arp.hwsrc}")
		print(f"Sestination MAC:  {arp.hwdst}")
		print(f"Source IP:  {arp.psrc}")
		print(f"Destination IP:  {arp.pdst}")

		return
	

	#IP Packet
	if packet.haslayer(IP):

		ip = packet[IP]

		print(f"Source IP:  {ip.src}")
		print(f"Destination IP: {ip.dst}")

		#ICMP
		if packet.haslayer(ICMP):
			print("Protocol:   ICMP")

		#TCP
		elif packet.haslayer(TCP):

			tcp = packet[TCP]

			print("Protocol:   tcp")
			print(f"Source Port:   {tcp.sport}")
			print(f"Destination Port:   {tcp.dport}")
			print(f"FLags:    {tcp.flags}")

		#UDP
		elif packet.haslayer(UDP):

			udp = packet[UDP]

			print("Protocol:   UDP")
			print(f"Source Port:   {udp.sport}")
			print(f"Destination Port:   {udp.dport}")

		else:
			print(f"Protocol:   {ip.proto}")


		#DNS
		if packet.haslayer(DNS):
			print("Application:   DNS")

		#Payload
		if packet.haslayer(Raw):

			payload = packet[Raw].load

			print(f"Payload length:   {len(payload)} bytes")

			#Display a safe printable representation
			try:
				readable = payload.decode(
					"utf-8",
					errors = "replace"
				)

				print(f"Payload preview:  {readable[:100]}")

			except Exception:
				print("Payload preview:   Binary data")

print("===================================================")
print("   BASIC PYTHON NETWORK SNIFFER ")
print("===================================================")
print("Starting packet capture...")
print("Press CTRL+C to stop.")
print()

sniff(
	prn=packet_callback,
	store=False
)
