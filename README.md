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

---
## PACKET ANALYSIS
---
| Field     | Description |
|--------   |-----------  |
| Source IP | IP address of the packet sender |
| Destination IP | IP address of the intended recipient |
| Protocol | Protocol identified in the packet, such as TCP, UDP, or ICMP |
| Source Port | Port associated with the sending endpoint |
| Destination Port | Port associated with the receiving endpoint |
| TCP Flags | Indicators of TCP connection and control operations |
| Payload | Data carried by the packet, which may be binary or encrypted |
| MAC Address | Hardware address used at the local network layer |

---
### Common protocols
---
- *TCP:* Reliable, connection-oriented transport.
- *UDP:* Connectionless transport used by services including many DNS queries.
- *ICMP:* Network diagnostic and error-reporting messages, including ping.
- *DNS:* Translates domain names into information such as IP addresses.
- *ARP:* Resolves IPv4 addresses to link-layer addresses on a local network.

---
## TESTING PROCEDURE
---
1. Start the Python sniffer.
2. Generate ICMP traffic with ping.
3. Generate DNS traffic with nslookup.
4. Generate HTTPS traffic with curl.
5. Observe the packet addresses, protocols, and ports.
6. If available, save a packet capture and inspect it with Wireshark.
7. Record actual observations and screenshots for the project report.

---
## SECURITY AND ETHICAL CONSIDERATIONS
---
Packet capture must only be performed on networks and devices that you own or are explicitly authorized to monitor. Captured traffic may contain sensitive information.

HTTPS/TLS encrypts application data, so a basic packet sniffer generally cannot read protected website content directly. Metadata such as IP addresses, ports, packet lengths, and timing may still be visible. Do not treat payload previews as proof that encrypted data has been decrypted.

Avoid committing PCAP files, credentials, tokens, personal information, or other sensitive traffic to a public repository. Use a controlled lab environment and sanitize screenshots before publishing them.

---
## LIMITATIONS
---
- Packet visibility depends on the selected interface and network configuration.
- Elevated privileges may be required.
- VirtualBox networking mode can affect which packets are visible.
- Encrypted application payloads are generally unreadable without authorized decryption and the necessary keys.
- The program is a learning tool, not a full-featured intrusion detection system.

---
## FUTURE IMPROVEMENTS
---
- Add command-line interface and protocol filters.
- Export packet summaries to CSV.
- Add packet counters and protocol statistics.
- Implement configurable capture limits and interface selection.
- Improve payload handling and output formatting.
- Integrate with Wireshark-compatible PCAP analysis workflows.

---
## LEARNING OUTCOMES
---
This project provides practical experience with Python, Scapy, packet capture, IP addressing, TCP/UDP ports, ICMP, DNS, packet layers, and basic network troubleshooting.

---
## CONCLUSION
---
The Basic Network Sniffer demonstrates how Python and Scapy can capture and inspect network traffic in an authorized environment. By examining packet headers and protocol information, the project helps explain how devices communicate and how different networking protocols operate. Optional PCAP analysis with Wireshark provides a more detailed view of packet structure.

---
## 👤 Author
---

Irabor Richard Ehis

CA/DF1/316498

LinkedIn: https://www.linkedin.com/in/richard-ehis-irabor-46b8899b/

---
## 📌 Project Information

Program Name: Cybersecurity at CodeAlpha | Project: Basic Network Sniffer using Python and Scapy | Repository: GitHub
