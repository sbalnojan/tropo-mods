import tropo_mods.auto_ec2 as auto_ec2
from troposphere import Template

t = Template()
my_instance = auto_ec2.AutoEc2(t, ami_name="ami-a12345678", asg=False)

my_instance.print_to_yaml()
