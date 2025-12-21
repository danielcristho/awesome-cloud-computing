# Infrastructure as Code

> IaC is the process of managing and provisioning infrastructure through machine-readable configuration files, rather than physical hardware or interactive configuration tools. It helps achieve consistency, scalability, and automation in cloud environments.

| Name | Description | Official Documentation |
|------|-------------|------|
| **Ansible** | An open-source automation tool for configuration management and application deployment, widely used for IaC. | [Ansible Community Documentation](https://www.ansible.com) |
| **AWS CDK** | Is an open-source software development framework for defining cloud infrastructure in code and provisioning it through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). | [AWS Cloud Development Kit](https://aws.amazon.com/cdk) |
| **Chef** | An open source systems management and cloud infrastructure automation platform. | [Chef Documentation](https://docs.chef.io) |
| **Pulumi** | Is an infrastructure-as-code platform for full-stack developers and cloud engineers who are interested in using a general-purpose programming language for their cloud resources. | [Pulumi Docs](https://www.pulumi.com/docs) |
| **Terraform** | IAC tool to provision and manage resources in any cloud or data center. | [Terraform Documentation](https://developer.hashicorp.com/terraform/docs) |
| **OpenTofu** | A community-driven open source fork of Terraform, fully compatible with existing Terraform configurations and providers. | [OpenTofu Documentation](https://opentofu.org/docs) |

## Tool Comparison

### Declarative vs Imperative

- **Declarative** (Terraform, Pulumi, AWS CDK) - Define desired end state
- **Imperative** (Ansible, Chef) - Define steps to achieve state

### Language Support

- **HCL** - Terraform, OpenTofu
- **YAML** - Ansible, CloudFormation
- **Programming Languages** - Pulumi (Python, TypeScript, Go, C#), AWS CDK (TypeScript, Python, Java, C#)
- **Ruby** - Chef

### Cloud Provider Support

- **Multi-cloud** - Terraform, Pulumi, Ansible
- **AWS-focused** - AWS CDK, CloudFormation
- **Agnostic** - Chef, Ansible

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*
