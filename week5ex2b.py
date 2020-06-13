#!/usr/bin/env python

from jinja2 import FileSystemLoader,StrictUndefined
from jinja2.environment import Environment

envmt=Environment(undefined=StrictUndefined)
filename=input("Enter the template file name:")
envmt.loader=FileSystemLoader('../donnie')

ip_address=['10.1.100.1','10.1.100.2']

interface_args={
'interface':'Ethernet1/1',
'ip_address':ip_address,
'peer_ip':ip_address[::-1],
'netmask':24,
'local_as':22
}
j2Template=envmt.get_template(filename)
intf_config=j2Template.render(**interface_args)
print(intf_config)

