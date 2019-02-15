''' ssh and get information about cisco switch using python and napalm '''
# Author: Anubhavsingh Sawdagur
# Created Date: 12 Febuary 2019

import json
from napalm_base import get_network_driver

IP_LIST = ["192.168.44.110", "192.168.44.111", "192.168.44.121", "192.168.44.122"]

for IP in IP_LIST:

    DRIVER = get_network_driver("ios")
    DEVICE = DRIVER(str(IP), "anubhav", "cisco")
    DEVICE.open()

    print("Connected to " + str(IP))
    # ------------------------------------
    print("Facts - " + str(IP))
    OUTPUT = DEVICE.get_facts()
    OUTPUT = json.dumps(OUTPUT, indent=4)
    print(OUTPUT)
    # ------------------------------------
    print("Interfaces - " + str(IP))
    OUTPUT = DEVICE.get_interfaces()
    OUTPUT = json.dumps(OUTPUT, sort_keys=True, indent=4)
    print(OUTPUT)
    # ------------------------------------
    print("Interfaces IP - " + str(IP))
    OUTPUT = DEVICE.get_interfaces_ip()
    OUTPUT = json.dumps(OUTPUT, sort_keys=True, indent=4)
    print(OUTPUT)
    # ------------------------------------
    print("MAC Address Table - " + str(IP))
    OUTPUT = DEVICE.get_mac_address_table()
    OUTPUT = json.dumps(OUTPUT, sort_keys=True, indent=4)
    print(OUTPUT)
    # ------------------------------------
    print("ARP Table - " + str(IP))
    OUTPUT = DEVICE.get_arp_table()
    OUTPUT = json.dumps(OUTPUT, sort_keys=True, indent=4)
    print(OUTPUT)
    # ------------------------------------
    print("BGP Neighbors - " + str(IP))
    OUTPUT = DEVICE.get_bgp_neighbors()
    OUTPUT = json.dumps(OUTPUT, sort_keys=True, indent=4)
    print(OUTPUT)

    DEVICE.close()
