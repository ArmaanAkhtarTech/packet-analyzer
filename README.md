# Network Packet Analyzer

## About

This is my fifth Python cybersecurity project.

I wanted to build this project to understand how network packets travel across a network and how they can be captured using Python. The program uses the Scapy library to capture live IP packets and then displays information such as the source IP address, destination IP address and the protocol being used.

While making this project I learnt more about packet sniffing, network traffic and how external Python libraries can be used within a cybersecurity program.

## Features

- Captures live IP packets
- Displays the source IP address
- Displays the destination IP address
- Detects TCP, UDP and ICMP packets
- Lets the user choose how many packets to capture
- Counts how many packets were captured
- Measures how long the capture took
- Handles unexpected errors

## Technologies Used

- Python
- Scapy
- Time module

## Example Output

```text
How many IP packets would you like to capture? 5

Packet Number: 1
Source IP: 192.168.0.84
Destination IP: 94.126.239.81
Protocol: TCP

Capture Summary

Packets captured: 5
Time taken: 3.42 seconds
```

## What I Learned

While making this project I learnt:

- How packet sniffing works
- How to use the Scapy library
- The difference between TCP, UDP and ICMP packets
- How callback functions work
- How to capture and display live packet information
- How to improve my error handling

## Future Improvements

If I continue working on this project I would like to:

- Display source and destination port numbers
- Save captured packet information to a text file
- Show more information about each packet
- Add protocol statistics
- Create a simple graphical interface
