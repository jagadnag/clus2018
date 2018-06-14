import requests
import json

"""
Modify these please
"""

f = open('switch_ip.txt', 'r')
for IP in f:
  IP = IP.strip('\n')
  url='http://%s/ins' % (IP)
  switchuser='admin'
  switchpassword='C1sco12345'
  print '\n' + '*' * 30
  print 'Switch IP ' + IP
  print '*' * 30
  myheaders={'content-type':'application/json-rpc'}
  payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show vlan",
      "version": 1
    },
    "id": 1
  }
  ]
  response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
  for id in response ['result']['body']['TABLE_vlanbrief']['ROW_vlanbrief']:
    x = id.get('vlanshowbr-vlanid')
    y = id.get('vlanshowbr-vlanname')
    print 'VLAN ID ' + (x) + ' ' + 'Name' + ' ' + (y)
