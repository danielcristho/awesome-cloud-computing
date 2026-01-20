# Edge Computing

> Platforms and tools for deploying and managing applications closer
> to end users and data sources, often outside centralized cloud regions.

| Name | Description | Link |
|------|-------------|------|
| **AWS Wavelength** | 5G edge computing service that brings AWS infrastructure to telecommunications networks. | [AWS Wavelength](https://aws.amazon.com/wavelength) |
| **AWS Local Zones** | AWS infrastructure deployments placed closer to population centers. | [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones) |
| **Azure Edge Zones** | Azure infrastructure services deployed closer to end users and devices. | [Azure Edge Zones](https://learn.microsoft.com/en-us/azure/extended-zones/overview) |
| **Google Distributed Cloud Edge** | Google Cloud infrastructure deployed at customer or edge locations. | [Distributed Cloud Edge](https://cloud.google.com/distributed-cloud/edge) |
| **AWS IoT Greengrass** | Service for running local compute, messaging, and data management on IoT devices. | [AWS IoT Greengrass](https://aws.amazon.com/greengrass) |
| **Azure IoT Edge** | Platform for deploying containerized workloads to IoT edge devices. | [Azure IoT Edge](https://azure.microsoft.com/en-us/products/iot-edge) |
| **K3s** | Lightweight Kubernetes distribution designed for edge and resource-constrained environments. | [K3s](https://k3s.io) |
| **OpenYurt** | Kubernetes-based edge computing framework extending cloud-native patterns to the edge. | [OpenYurt](https://openyurt.io) |

## Edge Computing Considerations

### Performance

- **Reduced latency** - Process data closer to where it is generated
- **Improved response times** - Faster application interactions
- **Real-time processing** - Support for time-sensitive workloads
- **Bandwidth optimization** - Minimize data transfer to centralized clouds

### Reliability

- **Offline tolerance** - Continued operation during connectivity loss
- **Distributed execution** - Reduced dependency on centralized systems
- **Local redundancy** - Multiple edge nodes for availability

### Cost Considerations

- **Reduced data transfer** - Lower bandwidth usage
- **Selective cloud usage** - Offload processing from central regions
- **Efficient scaling** - Scale compute closer to demand

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*

[:material-arrow-left: FinOps & Cost Management](finops-cost-management.md){ .md-button }
[:material-arrow-right: Monitoring](monitoring.md){ .md-button .md-button--primary }
