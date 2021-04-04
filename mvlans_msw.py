#!/usr/bin/python3

import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()
f = open("hosts")

for line in f:
    print ("Configuring switch: " + line.strip() + "\n")
    tn = telnetlib.Telnet(line.strip())

    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")

    for n in range (2,21):
        tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
        tn.write(b"name Python_VLAN_" + str(n).encode("ascii") + b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print (tn.read_all().decode("ascii"))
