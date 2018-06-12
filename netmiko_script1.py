#!/usr/bin/env python

from netmiko import ConnectHandler

nxos1 = {
    'device_type': 'cisco_nxos',
    'ip': '172.21.56.125',
    'username': 'admin',
    'password': 'cisco',
}

net_connect = ConnectHandler(**nxos1)
output = net_connect.send_command('show version')
print output
