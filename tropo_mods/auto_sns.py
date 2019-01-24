from troposphere import Parameter, Output, Ref, GetAtt, Base64
import troposphere.ec2 as ec2
import troposphere.iam as iam

# from awacs.aws import Allow, Statement, Principal, PolicyDocument
# from awacs.sts import AssumeRole


class AutoSNS:
    t = {}
    sshkey = ""
    asg = True
    key = True

    def __init__(self, t, topic_name, email):
        self.t = t
        self.construct_basics()

    def construct_basics(self):
        return None

    def print_to_yaml(self):
        print(self.t.to_yaml())
