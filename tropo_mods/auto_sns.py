from troposphere import Parameter, Output, Ref, GetAtt, Base64
import troposphere.sns as sns

# from awacs.aws import Allow, Statement, Principal, PolicyDocument
# from awacs.sts import AssumeRole


class AutoSNS:
    t = {}
    sshkey = ""
    asg = True
    key = True
    topic_name = ""

    def __init__(self, t, topic_name, email):
        self.t = t
        self.topic_name = topic_name
        self.construct_basics()

    def construct_basics(self):
        my_topic1 = sns.Topic("SNSTopic1", TopicName=self.topic_name)
        self.t.add_resource(my_topic1)

    def print_to_yaml(self):
        print(self.t.to_yaml())
        return self.t.to_yaml()
