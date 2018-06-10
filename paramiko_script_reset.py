import paramiko
import time

ip_address = "198.18.134.140"
username = "admin"
password = "C1sco12345"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Resetting Configuration on", ip_address

remote_connection = ssh_client.invoke_shell()

reset_config = ["configure terminal\n",
                "no interface loopback 0\n",
                "no interface loopback 1\n",
                "cdp timer 60\n",
                "no vlan 2-10\n",
                "hostname nxosv-1\n",
                "end\n"]

for line in reset_config:
    line=line.strip()
    print line
    remote_connection.send(line)
    time.sleep(0.5)

output = remote_connection.recv(65535)

ssh_client.close
