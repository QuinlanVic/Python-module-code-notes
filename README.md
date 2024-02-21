# **HTTP 2 vs HTTP 3**
## SDDA – 19 February 2024 
### By: Quinlan Caiger
HTTP/3 provides TLS encryption by default whereas HTTP/2 provides it as an optional feature. This extra security reduces the risks of the CIA triad being compromised such as through eavesdropping and MITM attacks. 

#### Some of its changes and benefits include
- Getting rid of TCP and using a new type of UDP called QUIC (Quick UDP Internet Connections)
  - QUIC provides the TLS encryption by default (no need for a separate TLS handshake)
- Reduced head-of-line blocking by dealing with each stream level of packet loss (lost packets don’t block all streams of information)
- Improved supporting connection migration meaning that when clients change IP addresses, they don’t lose connectivity or have additional delay
- Zero RTT connection establishment in specific situations (if already connected to a server you can skip the TCP handshake)
- Improved congestion control through advanced mechanisms

HTTP/3 sounds great in theory but is difficult to implement with compatibility issues surrounding networks.
