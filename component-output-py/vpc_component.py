from pulumi import  ResourceOptions
from typing import Optional
from pulumi_aws.ec2 import (
    Vpc,
    Subnet
)
from component_resource_output import *

class VpcComponent(ComponentResourceOutput):

    def __init__(self, name: str, opts: Optional[ResourceOptions] = None) -> None:
        super().__init__("pkg:index:vpcComponent", name, opts)

        vpc = Vpc("vpc", cidr_block="10.33.0.0/16")

        subnet = Subnet("subnet1", vpc_id=vpc.id, cidr_block="10.33.0.0/24")

        self.register_resources(resources=[
            vpc,
            subnet
        ])