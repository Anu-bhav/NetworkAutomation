''' ssh and get configure cisco routers and switches using python and napalm '''
# Author: Anubhavsingh Sawdagur
# Created Date: 12 Febuary 2019

from napalm_base import get_network_driver

IP_LIST = ["192.168.44.110", "192.168.44.111", "192.168.44.121", "192.168.44.122"]

for IP in IP_LIST:

    DRIVER = get_network_driver("ios")
    DEVICE = DRIVER(str(IP), "anubhav", "cisco")
    DEVICE.open()

    print("Connected to " + str(IP))
    print()
    DEVICE.load_merge_candidate(filename="Configurations\\IOSV_L3_Config.txt")
    DIFFERENCE = DEVICE.compare_config()

    if DIFFERENCE == '':
        print("No Loopback Changes Required")
        DEVICE.discard_config()
    else:
        print(DIFFERENCE)
        DEVICE.commit_config()

    print()

    DEVICE.close()
