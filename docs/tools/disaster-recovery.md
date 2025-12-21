# Disaster Recovery

> Solutions and tools for backup, disaster recovery, and business continuity in cloud environments.

| Name | Description | Link |
|------|-------------|------|
| **AWS Backup** | Centralized backup service to protect AWS services and hybrid workloads. | [AWS Backup](https://aws.amazon.com/backup/) |
| **Azure Site Recovery** | Disaster recovery as a service for replicating workloads from primary to secondary location. | [Azure Site Recovery](https://azure.microsoft.com/en-us/products/site-recovery/) |
| **Google Cloud Backup and DR** | Centralized backup and disaster recovery service for Google Cloud and hybrid environments. | [Backup and DR](https://cloud.google.com/backup-disaster-recovery) |
| **Veeam Backup & Replication** | Enterprise backup solution with cloud integration for hybrid environments. | [Veeam](https://www.veeam.com/backup-replication.html) |
| **Commvault** | Enterprise data protection platform with cloud backup and disaster recovery capabilities. | [Commvault](https://www.commvault.com/) |
| **Rubrik** | Cloud data management platform for backup, recovery, and data archival. | [Rubrik](https://www.rubrik.com/) |

## DR Components

### Recovery Objectives

- **RTO (Recovery Time Objective)** - Maximum acceptable downtime
- **RPO (Recovery Point Objective)** - Maximum acceptable data loss
- **RCO (Recovery Consistency Objective)** - Data consistency requirements
- **RLO (Recovery Level Objective)** - Granularity of recovery

### DR Patterns

- **Backup and Restore** - Lowest cost, highest RTO
- **Pilot Light** - Minimal infrastructure, moderate RTO
- **Warm Standby** - Scaled-down replica, lower RTO
- **Hot Standby/Multi-Site** - Full replica, lowest RTO

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*
