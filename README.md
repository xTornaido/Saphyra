# 🌊 Saphyra
 ## DDoS Script

  ```Don't use for malicious reasons. You can use it for testing, trolling your friends or learning from the code.```

  A distributed denial-of-service (DDoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic. DDoS attacks achieve effectiveness by utilizing multiple compromised computer systems as sources of attack traffic. Exploited machines can include computers and other networked resources such as IoT devices. From a high level, a DDoS attack is like an unexpected traffic jam clogging up the highway, preventing regular traffic from arriving at its destination.

  ### Layer 4
  <img align="left" alt="PNG" src="https://raw.githubusercontent.com/xTornaido/Saphyra/master/Layer-4/images/example.png" width="380" height="280" />
  Layer 4 DDoS attacks are often referred to as SYN flood. It works at the TCP (Transport Protocol) layer. A TCP connection is established in what is known as a 3-way handshake. The client sends a SYN packet, the server responds with a SYN-ACK, and the client responds to that with an ACK. after the "three-way-handshake" is complete, the TCP connection is considered established.

  Usage: ```python Saphyra-4.py {ip} {port} {time} {method}``` <br />
  Example: ```python Saphyra-4.py 127.0.0.1 8080 30 UDP-FLOOD```<br />
<br />
  ### Layer 7
  Layer 7 or application layer DDoS attacks attempt to overwhelm network or server resources with a flood of traffic (typically HTTP traffic). An example would be sending thousands of requests for a certain webpage per second until the server is overwhelmed and cannot respond to all of the requests. Another example would be calling an API over and over until the service crashes. Typically, layer 7 DDoS attacks are more complex than other kinds of DDoS attacks.

  Usage: ```python Saphyra-7.py {ip] {port} {time} {method}``` <br />
  Example: ```python Saphyra-7.py 127.0.0.1 443 30 FLOOD```