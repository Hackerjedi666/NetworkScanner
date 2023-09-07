import scapy.all as scapy
import asyncio
import optparse
from concurrent.futures import ThreadPoolExecutor

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP/IP range")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP address or IP range. Use -h for help.")
    return options

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_packet
    answered_list, _ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC ADDRESS\n------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

async def main():
    options = get_arguments()
    target = options.target
    loop = asyncio.get_running_loop()
    
    with ThreadPoolExecutor() as executor:
        scan_results = await loop.run_in_executor(executor, scan, target)
    
    print_result(scan_results)

if __name__ == "__main__":
    asyncio.run(main())
