#!/usr/bin/env python

from netmiko import ConnectHandler

nxos1 = {
    'device_type': 'cisco_nxos',
    'ip': '198.18.134.140',
    'username': 'admin',
    'password': 'C1sco12345',
}

net_connect = ConnectHandler(**nxos1)
output = net_connect.send_command('show version')
print output
