#! /usr/bin/env python

from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment

env=Environment()
env.loader=FileSystemLoader('.')
filename='vrf.j2'
vrf_vars={"vrf_name":"blue","rd_number":"100:1",'ipv4_enabled':True,'ipv6_enabled':True}
vrf_template=env.get_template(filename)
vrf_config=vrf_template.render(**vrf_vars)
print(vrf_config)

