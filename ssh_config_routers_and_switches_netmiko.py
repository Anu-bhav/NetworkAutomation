''' ssh and configure cisco switch using python and netmiko '''
# Author: Anubhavsingh Sawdagur
# Created Date: 11 Febuary 2019

from netmiko import ConnectHandler

IOSV_L3_R1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.44.110",
    "username": "anubhav",
    "password": "cisco",
}
IOSV_L3_R2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.44.111",
    "username": "anubhav",
    "password": "cisco",
}
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

with open("Networking\\Configurations\\IOSV_L3_Config.txt") as F:
    L3_COMMANDS = F.read().splitlines()
print(L3_COMMANDS)

with open("Networking\\Configurations\\IOU_L2_Config.txt") as F:
    L2_COMMANDS = F.read().splitlines()
print(L2_COMMANDS)

ALL_ROUTERS = [IOSV_L3_R1, IOSV_L3_R2]

for DEVICE in ALL_ROUTERS:
    NET_CONNECT = ConnectHandler(**DEVICE)
    print("Connected to " + DEVICE["ip"])
    OUTPUT = NET_CONNECT.send_command("sh ip int br")
    print(OUTPUT)
    OUTPUT = NET_CONNECT.send_config_set(L3_COMMANDS)
    print(OUTPUT)
    OUTPUT = NET_CONNECT.send_command("sh ip int br")
    print(OUTPUT)


ALL_SWITCHES = [IOU_L2_S1, IOU_L2_S2, IOU_L2_S3, IOU_L2_S4, IOU_L2_S5]

for DEVICE in ALL_SWITCHES:
    NET_CONNECT = ConnectHandler(**DEVICE)
    print("Connected to " + DEVICE["ip"])
    OUTPUT = NET_CONNECT.send_command("sh ip int br")
    print(OUTPUT)
    OUTPUT = NET_CONNECT.send_command("sh vlan br")
    print(OUTPUT)
    OUTPUT = NET_CONNECT.send_config_set(L2_COMMANDS)
    print(OUTPUT)
    OUTPUT = NET_CONNECT.send_command("sh vlan br")
    print(OUTPUT)
