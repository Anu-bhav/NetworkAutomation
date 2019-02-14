''' telnet and create loopback on cisco router using python '''
# Author: Anubhavsingh Sawdagur
# Created Date: 11 Febuary 2019

# import getpass
import telnetlib

HOST = "192.168.44.110"
USER = "anubhav"  # input("Enter your remote account: ")
PASSWORD = "cisco"  # getpass.getpass()

TN = telnetlib.Telnet(HOST, timeout=10)
# TN.set_debuglevel(1000)

TN.read_until(b"Username: ")
TN.write(USER.encode('ascii') + b"\n")
if PASSWORD:
    TN.read_until(b"Password: ")
    TN.write(PASSWORD.encode('ascii') + b"\n")

TN.write(b"term len 0\n")  # S1#
TN.write(b"sh ip int br\n")
TN.write(b"conf t\n")  # S1(config)#


# loop is 1 to 5
# for n in range(1, 6):
#     LOOP = "interface loopback " + str(n) + "\n"
#     TN.write(LOOP.encode('ascii') + b"\n")  # S1(config-if)#

#     IPADDR = "ip address " + str(n) + "." + str(n) + "." + str(n) + "." + str(n) + " 255.255.255.0\n"
#     TN.write(IPADDR.encode('ascii') + b"\n")
# TN.write(b"exit\n")  # S1(config)#

# To remove created Loopback interfaces
# -----------------------
for n in range(1, 6):
    LOOP = "no interface loopback " + str(n) + "\n"  # S1(config)#
    TN.write(LOOP.encode('ascii') + b"\n")
# -----------------------

TN.write(b"exit\n")
TN.write(b"sh ip int br\n")  # S1#
TN.write(b"wr\n")
TN.write(b"exit\n")

OUTPUT = TN.read_all().decode('ascii')
print(OUTPUT)
TN.close()
