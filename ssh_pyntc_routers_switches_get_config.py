''' ssh and get information about cisco switch using python and napalm '''
# Author: Anubhavsingh Sawdagur
# Created Date: 12 Febuary 2019

import os
import json
from pyntc import ntc_device as NTC

IP_LIST = ["192.168.44.110", "192.168.44.111", "192.168.44.121", "192.168.44.122"]
# IP_LIST = ["192.168.44.110"]

for IP in IP_LIST:

    DEVICE = NTC(host=str(IP), username='anubhav', password='cisco', device_type='cisco_ios_ssh')
    DEVICE.open()

    print("Connected to " + str(IP))

    # ------------------------------------
    print("Facts - " + str(IP))
    OUTPUT = DEVICE.facts
    OUTPUT = json.dumps(OUTPUT, indent=4)
    print(OUTPUT)

    # ------------------------------------
    print("Running Config - " + str(IP))
    OUTPUT = DEVICE.running_config
    print(OUTPUT)

    # ------------------------------------
    print("Backup of Running Config - " + str(IP))
    if not os.path.exists("Configuration Backup"):
        os.makedirs("Configuration Backup")
    FILENAME = "Configuration Backup\\device " + str(IP) + ".cfg"
    DEVICE.backup_running_config(FILENAME)
    print("Backup Completed for " + str(IP))

    # ------------------------------------

    DEVICE.close()
