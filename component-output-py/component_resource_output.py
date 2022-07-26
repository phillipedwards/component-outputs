from pulumi import ComponentResource, CustomResource, ResourceOptions, Inputs
from pulumi_aws.ec2 import Vpc
from typing import Optional, List

class ComponentResourceOutput(ComponentResource):
    resources: List[CustomResource]

    def __init__(self, t: str, name: str, props: Optional[Inputs] = None, opts: Optional[ResourceOptions] = None, remote: bool = False) -> None:
        super().__init__(t, name, props, opts, remote)

        self.resources = []

    def register_resource(self, resource: CustomResource):
        self.resources.append(resource)

    def register_resources(self, resources: List[CustomResource]):
        for resource in resources:
            self.register_resource(resource)