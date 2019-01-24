import tropo_mods.auto_sns as auto_sns
from troposphere import Template

test_sns_yaml = """\
Resources:
  SNSTopic1:
    Properties:
      TopicName: my_new_topic
    Type: AWS::SNS::Topic
"""

t = Template()
topic = auto_sns.AutoSNS(t, topic_name="my_new_topic", email="test@me.com")

assert test_sns_yaml == topic.print_to_yaml()
