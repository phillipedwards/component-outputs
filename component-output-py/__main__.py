"""An AWS Python Pulumi program"""

from pulumi import ResourceOptions
from vpc_component import *
from pulumi_aws import s3

vpc_comp = VpcComponent("vpc-comp")

bucket = s3.Bucket("bucket", opts=(ResourceOptions(depends_on=vpc_comp.resources)))
