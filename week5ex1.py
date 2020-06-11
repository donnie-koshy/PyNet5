#! usr/bin/env python
from jinja2 import Template

#Below is Jinja2 Template for generating BGP config
bgp_template='''
 router bgp {{local_as}}
  neighbor {{peer1_ip}} remote-as {{peer1_as}}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{peer2_ip}} remote-as {{peer2_as}}
    address-family ipv4 unicast'''

#Below are values or variable that are passed into above Template
bgp_values = {
'local_as':10,
'peer1_ip':'10.1.20.2',
'peer1_as':20,
'peer2_ip':'10.1.30.2',
'peer2_as':30
}

j2Template=Template(bgp_template)
bgp_config=j2Template.render(**bgp_values)
print ("BGP config")
print(bgp_config)

