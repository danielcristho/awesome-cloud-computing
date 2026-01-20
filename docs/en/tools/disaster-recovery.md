# Disaster Recovery

> Solutions and tools for backup, disaster recovery, and business continuity
> in cloud and hybrid environments.

| Name | Description | Link |
|------|-------------|------|
| **AWS Backup** | Centralized backup service for protecting AWS services and supported hybrid workloads. | [AWS Backup](https://aws.amazon.com/backup) |
| **Azure Site Recovery** | Disaster recovery service for replicating workloads between regions or locations. | [Azure Site Recovery](https://azure.microsoft.com/en-us/products/site-recovery) |
| **Google Cloud Backup and DR** | Managed backup and disaster recovery service for Google Cloud and hybrid environments. | [Backup and DR](https://cloud.google.com/backup-disaster-recovery) |
| **Veeam Backup & Replication** | Enterprise backup and replication solution with cloud and hybrid support. | [Veeam](https://www.veeam.com/products/veeam-data-platform/backup-recovery.html) |
| **Commvault** | Enterprise data protection platform for backup, recovery, and disaster recovery. | [Commvault](https://www.commvault.com) |
| **Rubrik** | Cloud data management platform for backup, recovery, and archival use cases. | [Rubrik](https://www.rubrik.com) |

## DR Components

### Recovery Objectives

- **RTO (Recovery Time Objective)** - Maximum acceptable downtime
- **RPO (Recovery Point Objective)** - Maximum acceptable data loss
- **RCO (Recovery Consistency Objective)** - Data consistency requirements after recovery
- **RLO (Recovery Level Objective)** - Granularity and scope of recovery

### DR Patterns

- **Backup and Restore** - Lowest cost, highest recovery time
- **Pilot Light** - Minimal infrastructure kept running
- **Warm Standby** - Scaled-down but functional environment
- **Hot Standby / Multi-Site** - Fully active replica with minimal downtime

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*

[:material-arrow-left: Cloud Migration](cloud-migration.md){ .md-button }
[:material-arrow-right: FinOps & Cost Management](finops-cost-management.md){ .md-button .md-button--primary }
