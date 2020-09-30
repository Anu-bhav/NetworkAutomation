''' telnet and get config of multiple cisco switches using python '''
# Author: Anubhavsingh Sawdagur
# Created Date: 11 Febuary 2019

import os
import telnetlib

USER = "anubhav"
PASSWORD = "cisco"
FILE = open("Networking\\switches.txt")

for LINE in FILE:
    HOST = LINE.strip()
    print("Telnet to IP: " + HOST)

    TN = telnetlib.Telnet(HOST, timeout=15)
    # TN.set_debuglevel(1000)

    TN.read_until(b"Username: ")
    TN.write(USER.encode("ascii") + b"\n")
    if PASSWORD:
        TN.read_until(b"Password: ")
        TN.write(PASSWORD.encode("ascii") + b"\n")
    TN.write(b"enable\n")
    TN.write(b"cisco\n")
    TN.write(b"conf t\n")
    TN.write(b"term len 0\n")  # S1#
    TN.write(b"show ip int br\n")
    TN.write(b"\n")
    TN.write(b"show vlan\n")
    TN.write(b"\n")
    TN.write(b"show run\n")
    TN.write(b"exit\n")

    OUTPUT = TN.read_all().decode('ascii')

    if not os.path.exists("Networking\\Switch Config Files"):
        os.makedirs("Networking\\Switch Config Files")

    SAVEFILE = open("Networking\\Switch Config Files\\switch " + HOST + ".txt", "w")
    SAVEFILE.write(OUTPUT)
    print(OUTPUT)
    TN.close()

FILE.close()
