# Containerization

> Is a technology that enables the packaging of applications and their dependencies into isolated containers, facilitating consistent deployment across different environments.

## Container Engines

| Name | Description | Link |
|------|-------------|------|
| **Docker** | Is a software platform that allows you to build, test, and deploy applications quickly using containers. | [Docker](https://www.docker.com/) |
| **Podman** | A daemonless container engine for managing OCI containers, providing a Docker-compatible CLI. | [Podman](https://podman.io/) |
| **containerd** | An industry-standard core container runtime used by Docker, Kubernetes, and other systems to manage container lifecycle. | [containerd](https://containerd.io/) |
| **Kata Containers** | An open-source OpenInfra project combining lightweight virtual machines with container speed, offering stronger isolation than standard containers. | [Kata Containers](https://katacontainers.io) |
| **Firecracker** | A lightweight microVM-based virtualization technology developed by AWS for running containers and serverless workloads securely and efficiently. | [Firecracker](https://firecracker-microvm.github.io) |

## Container Orchestration

| Name | Description | Link |
|------|-------------|------|
| **Kubernetes** | Is an open source system for automating deployment, scaling, and management of containerized applications. | [Kubernetes](https://kubernetes.io/) |
| **OpenShift** | A Kubernetes-based platform offering enterprise-grade security, monitoring, and tools. | [OpenShift](https://www.openshift.com/) |
| **Nomad** | A simple, flexible workload orchestrator that supports containers and non-containerized applications. | [Nomad](https://www.nomadproject.io/) |
| **Docker Swarm** | Is an advanced feature for managing a cluster of Docker daemons. | [Docker Swarm](https://docs.docker.com/engine/swarm/) |
| **AWS Fargate** | A serverless compute engine for containers that works with Amazon ECS and EKS, eliminating the need to manage servers. | [AWS Fargate](https://aws.amazon.com/fargate/) |
| **AWS EKS** | A managed Kubernetes service that simplifies running Kubernetes on AWS without the need to install or operate your own control plane. | [AWS EKS](https://aws.amazon.com/eks/) |
| **K3s** | A lightweight, certified Kubernetes distribution designed for resource-constrained environments such as IoT, edge, and development clusters. It is fully compliant with upstream Kubernetes. | [K3s](https://docs.k3s.io/) |
| **MicroK8s** | A lightweight, zero-ops Kubernetes distribution developed by Canonical (the company behind Ubuntu). Ideal for developers, edge, and CI/CD environments. | [MicroK8s](https://microk8s.io) |

## Management Tools

| Name | Description | Link |
|------|-------------|------|
| **Docker Compose** | A tool for defining and running multi-container Docker applications. | [Docker Compose](https://docs.docker.com/compose/) |
| **Helm** | A package manager for Kubernetes to deploy pre-configured applications as charts. | [Helm](https://helm.sh/) |
| **Portainer** | A container management software. | [Portainer](https://www.portainer.io/) |
| **Rancher** | A complete software stack for teams deploying containers, particularly Kubernetes clusters. | [Rancher](https://rancher.com/) |

## Container Benefits

### Development

- **Consistency** - Same environment from dev to production
- **Isolation** - Applications don't interfere with each other
- **Portability** - Run anywhere containers are supported
- **Efficiency** - Lightweight compared to virtual machines

### Operations

- **Scalability** - Easy horizontal scaling
- **Resource Utilization** - Better hardware utilization
- **Deployment Speed** - Fast startup and deployment
- **Rollback Capability** - Easy rollback to previous versions

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*

