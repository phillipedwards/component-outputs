import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";
import { ComponentResourceOutput } from "./componentResourceOutput";

export class VpcComponent extends ComponentResourceOutput {
    constructor(name: string, opts?: pulumi.ComponentResourceOptions) {
        super("index:pkg:compResource", name, {}, opts);

        const vpc = new awsx.ec2.Vpc("vpc", {
            cidrBlock: "10.25.0.0/16"
        });

        this.registerResource(vpc);
    }
}