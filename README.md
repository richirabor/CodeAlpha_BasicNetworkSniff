# codealpha_BasicNetworkSniff
# PROJECT TITLE: Implementation of a Basic Network Sniffer using Python and Scapy
---
## PROJECT OVERVIEW:
The Basic Network Sniffer is a Python-based networking project that captures and analyzes network packets using the Scapy library. It displays useful packet information, including source and destination IP addresses, protocols, port numbers, TCP flags, and selected payload data when available.

This project demonstrates fundamental networking concepts, packet inspection, and protocol analysis in a controlled and authorized lab environment.

---
## OBJECTIVES:
The task is to build a Python program that:

- Capture live network packets using Python.
- Identify source and destination IP addresses.
- Recognize TCP, UDP, ICMP, DNS, and ARP traffic where applicable.
- Display port numbers and TCP flags.
- Inspect limited payload information when available.
- Understand packet structure and network communication.
- Practice responsible network monitoring.

NOTE: Only sniffing traffic on my network interface was carried out for this project test.

---
## LAB ENVIRONMENT
---

- Python 3
- Scapy
- Kali Linux
- VirtualBox (optional)
- Wireshark (optional for detailed packet analysis)

---
## STRUCTURE
---

```text
Network Interface
       ↓
Scapy Packet Capture
       ↓
Python Callback
       ↓
Protocol Identification
       ↓
Packet Analysis
       ↓   
Wireshark Verification
````
---
## REQUIREMENTS

- Python 3 installed.
- Scapy installed.
- An active network interface.
- Appropriate privileges for packet capture.

---
### IMPLEMENTATION
---

#### Network Interface
---

<p align="center">
  <img src="Netwrk Intface.png"
      alt="Network Interface"
      width="800">
</p>

```text
ip addr
```
---

### Scapy Packet Structure
---

<p align="center">
  <img src="packet structure.png"
      alt="Scapy Packet"
      width="800">
</p>

```text
sudo scapy
```
---
## HOW TO RUN THE PROGRAM
---
Run the sniffer with the appropriate privileges:

<p align="center">
  <img src="ICMP Capture.png"
      alt="ICMP Capture"
      width="800">
</p>

```bash
sudo python3 sniffer.py
```
The program begins capturing packets and displays information as packets are observed. Press Ctrl+C to stop the capture.

Generate test traffic in a second terminal:

```bash
ping -c 4 8.8.8.8
nslookup example.com
curl https://example.com
```

These commands generate ICMP, DNS, ARP, and TCP/TLS-related traffic when the network and DNS configuration permit them. Actual results depend on the network environment.

---
## FEATURES
---
- Live packet capture.
- Source and destination IP identification.
- TCP, UDP, and ICMP protocol recognition.
- ARP address information.
- TCP and UDP port inspection.
- TCP flag inspection.
- DNS packet identification.
- Limited payload preview for packets containing a raw payload layer.
- Optional PCAP export for further analysis in Wireshark.

---
## OUTPUT SAMPLE
----
```text
==============================================
       BASIC PYTHON NETWORK SNIFFER
==============================================
Starting packet capture...
Press CTRL+C to stop.

======================================================================
Time: 07:00:29
Source IP:       10.0.2.15
Destination IP:  8.8.8.8
Protocol:        ICMP
```

The addresses and timestamps above are illustrative. Actual output will depend on the captured traffic.
