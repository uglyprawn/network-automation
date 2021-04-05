#!/usr/bin/python3

import paramiko
import time

ip_address = '1.1.2.1'
username = 'avram'
password = 'cisco'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = ip_address, username = username, password = password)

print("Connection succesful to: ", ip_address)

remote_connection = ssh_client.invoke_shell()

remote_connection.send("\n")
remote_connection.send("\n")
time.sleep(5)

remote_connection.send("config t\n")

for n in range(2,11):
    print('creating vlan: '+ str(n))
    remote_connection.send("vlan "+ str(n) + "\n")
    remote_connection.send("name Vlan " + str(n) + "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
#output = remote_connection.recv(65535)
#print(output)

ssh_client.close()