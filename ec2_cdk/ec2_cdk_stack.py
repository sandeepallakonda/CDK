from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class Ec2CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC with 2 Availability Zones
        vpc = ec2.Vpc(
            self,
            "MyVpc",
            max_azs=2
        )

        # Create a Security Group
        security_group = ec2.SecurityGroup(
            self,
            "EC2SecurityGroup",
            vpc=vpc,
            allow_all_outbound=True
        )

        # Allow SSH access
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow SSH access"
        )

        # Create EC2 Instance
        ec2.Instance(
            self,
            "MyEC2Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=vpc,
            security_group=security_group,
            key_name="ec2-key"
        )