''' ssh and create vlan on cisco switch using python and paramiko'''
# Author: Anubhavsingh Sawdagur
# Created Date: 11 Febuary 2019

import time
import paramiko

HOST = "192.168.44.121"
USER = "anubhav"  # input("Enter your remote account: ")
PASSWORD = "cisco"  # getpass.getpass()

SSH_CLIENT = paramiko.SSHClient()
SSH_CLIENT.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SSH_CLIENT.connect(hostname=HOST, username=USER, password=PASSWORD, look_for_keys=False, allow_agent=False)

print("Connecting to", HOST)
REMOTE_CONNECTION = SSH_CLIENT.invoke_shell()
print("Interactive SSH session established")
OUTPUT = REMOTE_CONNECTION.recv(1024)
print(OUTPUT.decode())

REMOTE_CONNECTION.send("\n")
REMOTE_CONNECTION.send("term len 0\n")  # S1#
REMOTE_CONNECTION.send("sh ip int br\n")
REMOTE_CONNECTION.send("conf t\n")  # S1(config)#
time.sleep(1)

for n in range(2, 6):
    VLAN = "interface vlan " + str(n) + "\n"
    REMOTE_CONNECTION.send(VLAN)  # S1(config-if)#
    REMOTE_CONNECTION.send("exit\n")  # S1(config)#

    GOTO_VLAN = "vlan " + str(n) + "\n"
    REMOTE_CONNECTION.send(GOTO_VLAN)  # S1(config-vlan)#

    VLAN_NAME = "name Python_Vlan_" + str(n) + "\n"
    REMOTE_CONNECTION.send(VLAN_NAME)
    REMOTE_CONNECTION.send("exit\n")  # S1(config)#
    time.sleep(0.5)
REMOTE_CONNECTION.send("exit\n")  # S1#


# To remove created Loopback interfaces
# -----------------------
# for n in range(2, 6):
#     VLAN = "no interface vlan " + str(n) + "\n"  # S1(config)#
#     REMOTE_CONNECTION.send(VLAN)
#     GOTO_VLAN = "no vlan " + str(n) + "\n"
#     REMOTE_CONNECTION.send(GOTO_VLAN)
#     time.sleep(0.5)
# REMOTE_CONNECTION.send("exit\n")  # S1#
# -----------------------

REMOTE_CONNECTION.send("sh vlan\n")
REMOTE_CONNECTION.send("wr\n")

REMOTE_CONNECTION.send("exit\n")

time.sleep(1)
OUTPUT = REMOTE_CONNECTION.recv(65535)
print(OUTPUT.decode())
