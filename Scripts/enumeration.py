#!/usr/bin/env python3
__author__      = "Zach Bennefield"

import os, sys,subprocess, zipfile, time
from sys import exit

#Am I running with root priv?
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again using 'su -' or 'sudo'. Exiting.")
#Upgrade distro. May want to disable for exam.
upgradedist = "apt update; apt dist-upgrade; apt autoremove; apt clean"
upgraderet = subprocess.run(upgradedist, shell=True)
#Grab some necessary files
toolinstall = "apt install man-db exploitdb; apt install python3 seclists curl enum4linux feroxbuster gobuster impacket-scripts nbtscan nikto nmap onesixtyone oscanner redis-tools smbclient smbmap snmp sslscan sipvicious tnscmd10g whatweb wkhtmltopdf; apt install python3-pip"
subprocess.run(toolinstall, shell=True)
#Let's make sure there is an IP file
while True:
   ipask = input('Do you have a file named iplist.txt?')
   if ipask.lower().startswith("n"):
      print("Please make one and rerun script")
      exit()
   elif ipask.lower().startswith("y"):
      print("Perfect!")
      break

#Make it easier to use IP list
def iplist():
    with open('iplist.txt', 'r') as f:
        iplist = f.read().replace('\n', '')
#Let's grab AutoRecon and store it for use. We are going to make an assumption Kali is being used for OSCP and install some packages
subprocess.run(['python3 -m pip install git+https://github.com/Tib3rius/AutoRecon.git'], shell=True)

