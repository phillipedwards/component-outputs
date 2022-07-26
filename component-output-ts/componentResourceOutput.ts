import * as pulumi from "@pulumi/pulumi";

export class ComponentResourceOutput extends pulumi.ComponentResource {

    public readonly resources: pulumi.CustomResource[];

    constructor(type: string, name: string, args?: pulumi.Inputs, opts?: pulumi.ComponentResourceOptions) {
        super(type, name, args, opts);

        this.resources = [];
    }

    registerResources(resources: pulumi.CustomResource[]) {
        resources.map(resource => {
            this.registerResource(resource);
        })
    }

    registerResource(resource: pulumi.CustomResource) {
        this.resources.push(resource);
    }
}