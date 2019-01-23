import tropo_mods.auto_ec2 as auto_ec2
from troposphere import Template, Join

t = Template()
my_instance = auto_ec2.AutoEc2(t, ami_name="ami-0eaec5838478eb0ba", asg=False)

my_instance.add_sg(port="3000", cidrIp="0.0.0.0/0")
my_instance.add_ud(Join("", ["#!/bin/bash -xe\n", "./home/ec2-user/my-app &"]))
my_instance.add_profile(access_to="codepipeline:*")

my_instance.print_to_yaml()
