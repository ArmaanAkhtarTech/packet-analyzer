# Network Packet Analyzer

## About

This is my fifth Python cybersecurity project.

The aim of this project was to get a better understanding of how network packets travel across a network and how they can be captured using Python. I used the Scapy library to capture live IP packets and display information such as the source IP address, destination IP address and the protocol being used.

Building this project also helped me become more confident using external Python libraries and working with network traffic.

## Features

- Captures live IP packets
- Shows the source IP address
- Shows the destination IP address
- Detects TCP, UDP and ICMP packets
- Lets the user choose how many packets to capture
- Counts how many packets were captured
- Shows how long the capture took
- Includes basic error handling

## Technologies Used

- Python
- Scapy
- Time module

## Example Output

How many IP packets would you like to capture? 5

Packet Number: 1
Source IP: 112.148.0.64
Destination IP: 91.136.246.81
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
- How callback functions work in Python
- How to count and display live packet information
- How to improve my error handling

## Future Improvements

In the future I would like to:

- Display port numbers
- Save packet information to a text file
- Show more information about each packet
- Add protocol statistics
- Create a simple GUI

## Author

Armaan Akhtar

BSc Computer Science for Cyber Security

University of Bradford