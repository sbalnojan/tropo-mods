from troposphere import Parameter, Output, Ref, Template, GetAtt, Export
import troposphere.ec2 as ec2


class AutoEc2:
    t = {}
    sshkey = ""
    asg = True

    def __init__(self,t,ami_name,asg=True):
        self.t=t
        self.ami_name = ami_name
        self.asg = True
        self.construct_basics()

    def construct_basics(self):

        my_param1 = Parameter("SshKeyName",
    Description="Name of an existing EC2 KeyPair to enable SSH "
                "access to the instance",
    Type="String")
        self.t.add_parameter(my_param1)

        my_instance1 = ec2.Instance("myinstance1", ImageId=self.ami_name, InstanceType="t1.micro",
                                    KeyName=Ref(my_param1),
                                    Tags=[{"key": "name", "value": "my_instance1"}])
        self.t.add_resource(my_instance1)

        self.t.add_output(Output(
        "PublicIP",
        Description="Public IP address of the newly created EC2 instance",
        Value=GetAtt(my_instance1, "PublicIp")))

    def print_to_yaml(self):
        print(self.t.to_yaml())
