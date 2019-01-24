import tropo_mods.auto_sns as auto_sns
from troposphere import Template

t = Template()
my_instance = auto_sns.AutoSNS(
    t, topic_name="my_new_topic", email="test@me.com"
)

my_instance.print_to_yaml()
