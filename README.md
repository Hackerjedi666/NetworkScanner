# NetworkScanner
# ARP Scanner with Scapy

This Python script allows you to perform an ARP scan on a target IP address or IP range using the Scapy library. ARP scanning can be used to discover devices within a local network and obtain their IP and MAC addresses.

## Prerequisites

Before you can run the script, make sure you have the following prerequisites installed:

- Python 3.x
- Scapy library

You can install Scapy using pip:

```pip install scapy```


## Usage

1. Clone this repository to your local machine:

```git clone https://github.com/Hackerjedi666/NetworkScanner.git```


2. Navigate to the project directory:

```cd NetworkScanner```

3. Run the ARP scanner script with the `-t` or `--target` flag followed by the target IP address or IP range:

```python arp_scanner.py -t 192.168.1.1/24```


Replace `192.168.1.1/24` with your target IP or IP range.

## Example Output

The script will display the discovered devices along with their IP and MAC addresses in the following format:

```
IP MAC ADDRESS
192.168.1.1 00:1a:2b:3c:4d:5e
192.168.1.2 00:2a:3b:4c:5d:6e
...
```

## Acknowledgments

- Thanks to the Scapy project for providing a powerful packet manipulation library.
- This script is for educational purposes and should be used responsibly.

Feel free to contribute to this project by creating issues, suggesting improvements, or adding new features.

