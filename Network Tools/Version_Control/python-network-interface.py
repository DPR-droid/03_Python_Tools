# https://www.geeksforgeeks.org/python-network-interface/
# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
# Import libraries
import socket
import netifaces as ni
import ipaddress
import json

def get_local_ip_addresses():
    try:
        # Get the hostname of the local machine
        hostname = socket.gethostname()

        # Resolve all local IP addresses associated with the hostname
        local_ips = socket.gethostbyname_ex(hostname)[2]

        # Filter out loopback addresses (e.g., 127.0.0.1)
        local_ips = [ip for ip in local_ips if not ip.startswith("127.")]

        # Get the network interfaces
        interfaces = ni.interfaces()

        subnet_info = {}
        for interface in interfaces:
            try:
                addrs = ni.ifaddresses(interface)
                ipv4_info = addrs[ni.AF_INET][0]
                ip = ipv4_info['addr']
                netmask = ipv4_info['netmask']

                network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                subnet_info[interface] = {
                    'ip': ip,
                    'subnet': str(network.network_address),
                    'netmask': netmask,
                }
            except (ValueError, KeyError):
                pass

        return {'local_ips': local_ips, 'subnet_info': subnet_info}
    except Exception as e:
        return None

# Example usage:
result = get_local_ip_addresses()
if result:
    print(json.dumps(result, indent=4))
else:
    print("Unable to retrieve local IP addresses and subnet information.")