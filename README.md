# codealpha_BasicNetworkSniff
# PROJECT TITLE: Implementation of a Basic Network Sniffer using Python and Scapy
---
## INTRODUCTION:
For a basic network sniffer practical, this involves the development 
of a Python-based packet sniffer to observe the network traffic and 
understand the fundamental networking protocols such as TCP, UDP, ICMP, IP, and DNS. 

The purpose is to capture the network packets, analyze the structure, 
and identify the communication protocols and useful information 
from the captured traffic. 

---
## OBJECTIVES:
The task is to build a Python program that:

- Captures Live network packets.
- Identifies Source and Destination IP addresses.
- Identifies protocols such as TCP, UDP, ICMP, DNS, and ARP.
- Displays useful packet information.
- Examines packet structure and selected payload data.
- Demonstrates how information flows between network devices.

NOTE: Only sniffing traffic on my network interface was carried out for this project test.

---
## LAB ENVIRONMENT
---

- Python 3
- Scapy
- Kali Linux
- VirtualBox
- Wireshark

---
## METHODOLOGY
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

### Python Source code 
---

```text
src="sniffer.py"
```

