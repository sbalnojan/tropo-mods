# tropo-mods

Write 10 times less CloudFormation using tropo-mods (a catalog of troposphere code). Defining infrastructure
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
        
````
### Next Up 1

````python
my_instance = auto_ec2()
my_instance.add_sg(port=3000,cidrIp="0.0.0.0/0")
my_instance.add_ud("!Sub | #!/bin/bash -xe "\
            "./home/ec2-user/my-app &")
````
should turn into an instance running our app, open to any http traffic on port 3000.
````bash
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: "t2.micro"
      SecurityGroups:
      - Ref: InstanceSecurityGroup
      ImageId: "ami-0000"
      IamInstanceProfile: !Ref InstanceProfile
      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash -xe
            ./home/ec2-user/my-app &

````
### Next Up 2
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