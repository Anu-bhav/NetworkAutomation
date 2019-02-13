''' ssh and get configure cisco routers using python and napalm '''
# Author: Anubhavsingh Sawdagur
# Created Date: 12 Febuary 2019

from napalm_base import get_network_driver

IP_LIST = ["192.168.44.110"]

for IP in IP_LIST:

    DRIVER = get_network_driver("ios")
    IOS_L3 = DRIVER(str(IP), "anubhav", "cisco")
    IOS_L3.open()

    print("Connected to " + str(IP))

    IOS_L3.load_merge_candidate(filename="Networking\\Configurations\\IOSV_L3_Config.txt")

    DIFFERENCE = IOS_L3.compare_config()
    print(DIFFERENCE)
    # if len(DIFFERENCE) > 0:
    #     print(DIFFERENCE)
    #     print()
    #     IOS_L3.commit_config()
    # else:
    #     print("No Loopback Changes Required")
    #     print()
    #     IOS_L3.discard_config()

    IOS_L3.close()
