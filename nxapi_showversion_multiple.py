import requests
import json
import sys

"""
Modify these please
"""
f = open('devices_list', 'r')
for IP in f:
	IP = IP.strip('\n')
	url='http://%s/ins' % (IP)
	switchuser='admin'
	switchpassword='C1sco12345'

	myheaders={'content-type':'application/json-rpc'}
	payload=[
	{
	"jsonrpc": "2.0",
	"method": "cli",
	"params": {
	  "cmd": "show version",
	  "version": 1
	},
	"id": 1
	}
	]
	response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
	print "Switch IP " + IP + " " + "NX-OS Version %s" % response['result']['body']['kickstart_ver_str']
