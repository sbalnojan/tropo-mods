from troposphere import Parameter, Output, Ref, GetAtt, Base64
import troposphere.ec2 as ec2
import troposphere.iam as iam

# from awacs.aws import Allow, Statement, Principal, PolicyDocument
# from awacs.sts import AssumeRole


class AutoEc2:
    t = {}
    sshkey = ""
    asg = True
    key = True

    def __init__(self, t, ami_name, asg=True, key=True):
        self.t = t
        self.ami_name = ami_name
        self.asg = asg
        self.key = key
        self.construct_basics()

    def construct_basics(self):
        my_instance1 = ec2.Instance(
            "myinstance1",
            ImageId=self.ami_name,
            InstanceType="t2.micro",
            Tags=[{"Key": "name", "Value": "my_instance1"}],
        )

        if self.key:
            my_param1 = Parameter(
                "SshKeyName",
                Description="Name of an existing EC2 KeyPair to enable SSH "
                "access to the instance",
                Type="String",
            )
            self.t.add_parameter(my_param1)

            my_instance1 = ec2.Instance(
                "myinstance1",
                ImageId=self.ami_name,
                InstanceType="t2.micro",
                KeyName=Ref(my_param1),
                Tags=[{"Key": "name", "Value": "my_instance1"}],
            )

        self.t.add_resource(my_instance1)

        self.t.add_output(
            Output(
                "PublicIP",
                Description="Public IP address of the newly created "
                "EC2 instance",
                Value=GetAtt(my_instance1, "PublicIp"),
            )
        )

    def add_sg(self, port, cidrIp):
        instance_security_group_rule = ec2.SecurityGroupRule(
            IpProtocol="tcp", FromPort=port, ToPort=port, CidrIp=cidrIp
        )

        # Security group that's applied to the Mount Targets.
        instance_security_group = ec2.SecurityGroup(
            "SecurityGroup1",
            SecurityGroupIngress=[instance_security_group_rule],
            GroupDescription="Allow NFS over TCP",
        )
        self.t.add_resource(instance_security_group)
        self.t.resources["myinstance1"].properties["SecurityGroups"] = [
            Ref(instance_security_group)
        ]

    def add_ud(self, user_data):
        self.t.resources["myinstance1"].properties["UserData"] = Base64(
            user_data
        )

    def add_profile(self, access_to):
        InstancePolicy1 = iam.Policy(
            "InstancePolicy1",
            PolicyName="InstancePolicy1",
            PolicyDocument={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": [access_to],
                        "Resource": ["*"],
                        "Effect": "Allow",
                    }
                ],
            },
        )
        role = iam.Role(
            "InstanceRole1",
            AssumeRolePolicyDocument={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Principal": {"Service": "ec2.amazonaws.com"},
                        "Effect": "Allow",
                    }
                ],
            },
            Policies=[InstancePolicy1],
        )
        profile = iam.InstanceProfile(
            "InstanceProfile1",
            Roles=[Ref(role)],
            InstanceProfileName="someString",
        )
        self.t.add_resource(role)
        self.t.add_resource(profile)

    def print_to_yaml(self):
        print(self.t.to_yaml())
