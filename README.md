# tropo-mods

Write 10 times less Cloudformation using tropo-mods (a module catalog for troposphere). Defining infrastructure
should be this simple:
````python
import tropo_mods.auto_ec2 as auto_ec2
my_instance = auto_ec2(ami="ami-a12345678", asg=False)

print(my_instance.to_yaml())
````

should produce
````bash
Parameters: 
  SshKeyName: 
    Type: String
    Default: testKey
    
Resources:
    myinstance1:
        Properties:
            ImageId: ami-a12345678
            InstanceType: t1.micro
        Type: AWS::EC2::Instance
        KeyName: !Ref SshKeyName
        Tags:
            - Key: Name
              Value: myinstance1

Outputs:
  Output1:
    Description: myinstance1 public IP
    Value: !GetAtt myinstance1.PublicIp
    Export:
      Name: myinstance1PublicIp
        
````

Code like
````python
my_instance = auto_ec2(asg=False)
my_instance.add_sg(127.0.0.1)
````
should produce an instance only accessible via SSH/TCP from 127.0.0.1 and code like

````python
my_instance = auto_ec2(ami="ami-a12345678")

print(my_instance.to_yaml())
````
should produce an ec2 instance with an auto scaling group.