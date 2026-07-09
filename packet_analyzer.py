from scapy.all import sniff, IP, TCP, UDP, ICMP
import time

# ==========================================
# Packet Analyzer
# This is my fifth Python cybersecurity project.
# It captures live network packets and shows
# basic details about the traffic.
# ==========================================

# This keeps count of the packets we actually show
packet_count = 0

# Ask the user how many packets they want
number_of_packets = int(input("How many IP packets would you like to capture? "))

# Start the timer
start_time = time.time()


# This function runs every time Scapy finds a packet
def analyse_packet(packet):

    global packet_count

    # This should only run for packets that have an IP layer
    # because of the filter in the sniff() function below
    packet_count = packet_count + 1

    # Get the source and destination IP addresses
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    # Work out the protocol
    if TCP in packet:
        protocol = "TCP"

    elif UDP in packet:
        protocol = "UDP"

    elif ICMP in packet:
        protocol = "ICMP"

    else:
        protocol = "Other"

    # Print the packet details
    print("\n----------------------------------------")
    print("Packet Number:", packet_count)
    print("Source IP:", source_ip)
    print("Destination IP:", destination_ip)
    print("Protocol:", protocol)
    print("----------------------------------------")


print("\n========================================")
print("      Simple Network Packet Analyzer")
print("========================================")
print("Listening for network traffic...")
print("Only IP packets will be shown.")
print("Capturing", number_of_packets, "packets...")
print("Press CTRL + C to stop early.\n")


try:

    # Start capturing packets
    # lfilter makes sure we only capture packets that have an IP layer
    sniff(
        prn=analyse_packet,
        count=number_of_packets,
        store=False,
        lfilter=lambda packet: IP in packet
    )

    # End the timer
    end_time = time.time()

    print("\n========================================")
    print("Capture Summary")
    print("========================================")
    print("Packets captured:", packet_count)
    print("Time taken:", round(end_time - start_time, 2), "seconds")
    print("Capture complete.")

except KeyboardInterrupt:

    end_time = time.time()

    print("\nCapture stopped by user.")
    print("Packets captured:", packet_count)
    print("Time taken:", round(end_time - start_time, 2), "seconds")

except Exception as error:

    print("\nSomething went wrong while capturing packets.")
    print(error)