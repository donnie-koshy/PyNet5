#!/usr/bin/env python

from jinja2 import FileSystemLoader,StrictUndefined
from jinja2.environment import Environment
#from getpass import getpass
from netmiko import ConnectHandler
from my_devices import nxos1,nxos2

import time

envmt=Environment(undefined=StrictUndefined)
filename=input("Enter the template file name:")
envmt.loader=FileSystemLoader('.')


ip_address=['10.1.100.1','10.1.100.2']
peer_ip=ip_address[::-1]
device=[nxos1,nxos2]

j2Template=envmt.get_template(filename)

for i in range(len(ip_address)):
    router_args={'interface':'Ethernet1/1','ip_address':ip_address[i],'peer_ip':peer_ip[i],'netmask':24,'local_as':22}
    rtr_config=j2Template.render(**router_args)        
    rtr_config_list=rtr_config.splitlines()
    net_connect=ConnectHandler(**device[i])
    print("Logged into "+net_connect.find_prompt().strip('#'))
    net_connect.send_config_set(rtr_config_list)
    if '#' in net_connect.find_prompt():
        print ("Configuration applied successfully")

time.sleep(60.0)
bgp_status=net_connect.send_command("show ip bgp summary")
print(bgp_status)        

net_connect.disconnect()


print ("Device 1 status")
print(statusCheck(nxos1))

def statusCheck(device):
    i=0
    net_connect=ConnectHandler(**device)
    print ("Ping status")
    net_connect.send_command("ping"+ip_address[i+1])
    print ("\n BGP status")
    net_connect.send_command("show ip bgp summary")
