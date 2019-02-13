''' ssh and create vlan on cisco switch using python and netmiko '''
# Author: Anubhavsingh Sawdagur
# Created Date: 11 Febuary 2019

from netmiko import ConnectHandler

IOU_L2_S1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.44.121",
    "username": "anubhav",
    "password": "cisco",
}
IOU_L2_S2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.44.122",
    "username": "anubhav",
    "password": "cisco",
}
IOU_L2_S3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.44.123",
    "username": "anubhav",
    "password": "cisco",
}
IOU_L2_S4 = {
    "device_type": "cisco_ios",
    "ip": "192.168.44.124",
    "username": "anubhav",
    "password": "cisco",
}
IOU_L2_S5 = {
    "device_type": "cisco_ios",
    "ip": "192.168.44.125",
    "username": "anubhav",
    "password": "cisco",
}

ALL_DEVICES = [IOU_L2_S1, IOU_L2_S2, IOU_L2_S3, IOU_L2_S4, IOU_L2_S5]

for DEVICE in ALL_DEVICES:
    NET_CONNECT = ConnectHandler(**DEVICE)
    print("Connected to " + DEVICE["ip"])
    OUTPUT = NET_CONNECT.send_command("sh ip int br")
    print(OUTPUT)

    # for n in range(2, 6):
    #     VLAN = "interface vlan " + str(n)
    #     GOTO_VLAN = "vlan " + str(n)
    #     VLAN_NAME = "name Python_Vlan_" + str(n)
    #     CONFIG_COMMAND = [VLAN, GOTO_VLAN, VLAN_NAME]
    #     OUTPUT = NET_CONNECT.send_config_set(CONFIG_COMMAND)
    #     print(OUTPUT)

    # To remove created Loopback interfaces
    # -----------------------
    for n in range(2, 6):
        VLAN = "no interface vlan " + str(n)
        GOTO_VLAN = "no vlan " + str(n)
        CONFIG_COMMAND = [VLAN, GOTO_VLAN]
        OUTPUT = NET_CONNECT.send_config_set(CONFIG_COMMAND)
        print(OUTPUT)
    # -----------------------
    OUTPUT = NET_CONNECT.send_command("sh vlan")
    print(OUTPUT)
