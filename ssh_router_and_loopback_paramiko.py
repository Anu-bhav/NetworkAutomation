''' telnet and create loopback on cisco router using python and paramiko'''
# Author: Anubhavsingh Sawdagur
# Created Date: 11 Febuary 2019

import time
import paramiko

HOST = "192.168.44.110"
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

# for n in range(1, 6):
#     LOOP = "interface loopback " + str(n) + "\n"
#     REMOTE_CONNECTION.send(LOOP)  # S1(config-if)#

#     IPADDR = "ip address " + str(n) + "." + str(n) + "." + str(n) + "." + str(n) + " 255.255.255.0\n"
#     REMOTE_CONNECTION.send(IPADDR)
#     time.sleep(0.5)
# REMOTE_CONNECTION.send("exit\n")  # S1(config)#

# To remove created Loopback interfaces
# -----------------------
for n in range(1, 6):
    LOOP = "no interface loopback " + str(n) + "\n"
    REMOTE_CONNECTION.send(LOOP)  # S1(config)#
    time.sleep(0.5)
# -----------------------

REMOTE_CONNECTION.send("exit\n")  # S1#
REMOTE_CONNECTION.send("sh ip int br\n")
REMOTE_CONNECTION.send("wr\n")
time.sleep(5)
REMOTE_CONNECTION.send("exit\n")
OUTPUT = REMOTE_CONNECTION.recv(65535)
print(OUTPUT.decode())
