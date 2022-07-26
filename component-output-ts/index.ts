import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import { VpcComponent } from "./vpcComponent";

const bucketComp = new VpcComponent("vpc-comp");

const bucket = new aws.s3.Bucket("bucket", {});

const vpc = <awsx.ec2.Vpc>bucketComp.resources[0];

export const bucketId = bucket.bucket;
export const vpcId = vpc.id;