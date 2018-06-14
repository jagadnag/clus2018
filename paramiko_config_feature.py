import paramiko
import time

ip_address = "198.18.134.140"
username = "admin"
password = "C1sco12345"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("feature nxapi\n")
remote_connection.send("end\n")
time.sleep(1)

output = remote_connection.recv(65535)
print output

ssh_client.close