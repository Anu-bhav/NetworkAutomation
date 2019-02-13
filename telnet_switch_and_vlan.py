''' telnet and create vlan on cisco switch using python '''
# Author: Anubhavsingh Sawdagur
# Created Date: 11 Febuary 2019

import telnetlib

HOST = "192.168.44.121"
USER = "anubhav"
PASSWORD = "cisco"

TN = telnetlib.Telnet(HOST, timeout=15)
# TN.set_debuglevel(1000)

TN.read_until(b"Username: ")
TN.write(USER.encode("ascii") + b"\n")
if PASSWORD:
    TN.read_until(b"Password: ")
    TN.write(PASSWORD.encode("ascii") + b"\n")

TN.write(b"term len 0\n")  # S1#
TN.write(b"sh ip int br\n")
TN.write(b"conf t\n")  # S1(config)#

for n in range(2, 6):
    VLAN = "interface vlan " + str(n)
    TN.write(VLAN.encode("ascii") + b"\n")   # S1(config-if)#
    TN.write(b"exit\n")  # S1(config)#

    GOTO_VLAN = "vlan " + str(n)
    TN.write(GOTO_VLAN.encode("ascii") + b"\n")  # S1(config-vlan)#

    VLAN_NAME = "name Python_Vlan_" + str(n)
    TN.write(VLAN_NAME.encode("ascii") + b"\n")
    TN.write(b"exit\n")  # S1(config)#
TN.write(b"exit\n")  # S1#

# To remove created vlans
# -----------------------
# for n in range(2, 6):
#     VLAN = "no interface vlan " + str(n) # S1(config)#
#     TN.write(VLAN.encode("ascii") + b"\n")
#     GOTO_VLAN = "no vlan " + str(n)
#     TN.write(GOTO_VLAN.encode("ascii") + b"\n")  # S1(config)#
# TN.write(b"exit\n")  # S1#
# -----------------------

TN.write(b"sh vlan br\n")
TN.write(b"wr\n")
TN.write(b"exit\n")

OUTPUT = TN.read_all().decode('ascii')
print(OUTPUT)
TN.close()
