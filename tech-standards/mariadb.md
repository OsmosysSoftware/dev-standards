# MariaDB Configuration Guide

## Table of Contents

1. [Introduction](#introduction)
   - [What is MariaDB?](#what-is-mariadb)
   - [Importance of Configuration](#importance-of-configuration)
   - [Scope of This Guide](#scope-of-this-guide)

2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Accessing the `my.cnf` File](#accessing-the-mycnf-file)
   - [Backup and Restore Best Practices](#backup-and-restore-best-practices)

3. [Core Configuration Parameters](#core-configuration-parameters)
   - [General Settings](#general-settings)
   - [Data Directory and File Paths](#data-directory-and-file-paths)

4. [Storage Engines](#storage-engines)
   - [InnoDB Configuration](#innodb-configuration)
     - [Buffer Pool Size](#buffer-pool-size)
     - [Log File Size](#log-file-size)
     - [Flush Methods](#flush-methods)
     - [ACID Compliance Options](#acid-compliance-options)
   - [File-Per-Table Option](#file-per-table-option)
   - [Other Storage Engines Overview](#other-storage-engines-overview)

5. [Performance Optimization](#performance-optimization)
   - [Query Cache Configuration](#query-cache-configuration)
     - [Enabling/Disabling Query Cache](#enablingdisabling-query-cache)
     - [Sizing the Query Cache](#sizing-the-query-cache)
   - [Temporary Table Settings](#temporary-table-settings)
   - [Thread and Connection Handling](#thread-and-connection-handling)
   - [Buffer Pool Instances](#buffer-pool-instances)

6. [Logging and Monitoring](#logging-and-monitoring)
   - [Slow Query Logs](#slow-query-logs)
     - [Enabling and Configuring Slow Query Logs](#enabling-and-configuring-slow-query-logs)
     - [`long_query_time` Threshold](#long_query_time-threshold)
   - [Log Verbosity Options](#log-verbosity-options)
   - [Monitoring Tools](#monitoring-tools)

7. [I/O and Disk Configuration](#io-and-disk-configuration)
   - [I/O Capacity Settings](#io-capacity-settings)
   - [Swappiness and Kernel Settings](#swappiness-and-kernel-settings)
   - [File System and I/O Scheduler Recommendations](#file-system-and-io-scheduler-recommendations)

8. [Advanced Settings](#advanced-settings)
   - [Replication Configuration](#replication-configuration)
     - [Master-Slave and Multi-Master Replication](#master-slave-and-multi-master-replication)
     - [Binlog Settings](#binlog-settings)
   - [Galera Cluster Configuration](#galera-cluster-configuration)
   - [Security Best Practices](#security-best-practices)

9. [OS and Hardware Considerations](#os-and-hardware-considerations)
    - [Optimizing for SSDs and HDDs](#optimizing-for-ssds-and-hdds)
    - [Swappiness Settings](#swappiness-settings)
    - [CPU and Memory Optimization](#cpu-and-memory-optimization)

10. [Common Pitfalls and Troubleshooting](#common-pitfalls-and-troubleshooting)
    - [Avoiding Query Cache Misconfigurations](#avoiding-query-cache-misconfigurations)
    - [Common Error Logs and Solutions](#common-error-logs-and-solutions)
    - [Handling High CPU or Memory Usage](#handling-high-cpu-or-memory-usage)

11. [Sample Configurations](#sample-configurations)
   - [Small Server Setup (2 CPUs, 4 GB RAM)](#small-server-setup-2-cpus-4-gb-ram)
   - [Medium Server Setup (4 CPUs, 8 GB RAM)](#medium-server-setup-4-cpus-8-gb-ram)
   - [Large Server Setup (8 CPUs, 16 GB RAM)](#large-server-setup-8-cpus-16-gb-ram)
   - [High-Performance Server Setup (16+ CPUs, 64 GB RAM)](#high-performance-server-setup-16-cpus-64-gb-ram)

12. [References](#references)
    - [Official MariaDB Documentation](#official-mariadb-documentation)
    - [Third-Party Resources](#third-party-resources)
    - [Tools and Utilities](#tools-and-utilities)

---

## Introduction

### What is MariaDB?
MariaDB is a robust, open-source relational database management system (RDBMS) that originated as a fork of MySQL. It is designed to provide scalability, performance, and advanced features, making it ideal for enterprise and community use.

### Importance of Configuration
Proper configuration ensures optimal performance, scalability, and reliability of your database system. Tailoring settings to your specific server hardware and workload is critical.

### Scope of This Guide
This guide is a comprehensive resource to configure and optimize MariaDB effectively, including examples, best practices, and troubleshooting tips.

---

## Getting Started

### Installation
1. **Ubuntu**: `sudo apt install mariadb-server`
2. **CentOS**: `sudo yum install mariadb-server`
3. **Windows**: Download and install from the [official MariaDB website](https://mariadb.org/).

### Accessing the `my.cnf` File
The primary configuration file for MariaDB is `my.cnf`. Default locations:
- **Linux**: `/etc/mysql/my.cnf` or `/etc/my.cnf`
- **Windows**: `C:\Program Files\MariaDB\`.

### Backup and Restore Best Practices
- Use `mysqldump` for logical backups: `mysqldump -u [user] -p [database] > backup.sql`
- Use physical backups for large databases: [MariaDB Backup](https://mariadb.com/kb/en/mariabackup/).

---

## Core Configuration Parameters

### General Settings
```ini
[mysqld]
user = mysql
port = 3306
socket = /var/lib/mysql/mysql.sock
datadir = /var/lib/mysql
```

### Data Directory and File Paths
Ensure sufficient disk space and use fast disks (SSDs preferred). Example:
```ini
datadir = /mnt/data/mysql
log_error = /var/log/mysql/error.log
```

---

## Storage Engines

### InnoDB Configuration

#### Buffer Pool Size
The `innodb_buffer_pool_size` parameter determines the amount of memory allocated to the InnoDB buffer pool, which caches data and indexes. A larger buffer pool improves performance by reducing disk I/O.

**Recommendation**: Set this to 70-80% of the available RAM on your server.
```ini
innodb_buffer_pool_size = 6G
```

#### Log File Size
The `innodb_log_file_size` specifies the size of each InnoDB log file. Larger log files improve write performance but may increase recovery time after a crash.

**Recommendation**: Set this based on workload. For most servers:
```ini
innodb_log_file_size = 1G
```

#### Flush Methods
The `innodb_flush_method` determines how data is written to disk. 

**Recommendation**: Use `O_DIRECT` for SSDs to bypass the operating system cache and reduce double buffering.
```ini
innodb_flush_method = O_DIRECT
```

#### ACID Compliance Options
The `innodb_flush_log_at_trx_commit` parameter controls how often logs are flushed to disk. This affects durability and performance:
- **1**: Full ACID compliance (flush on every transaction commit).
- **2**: Flush once per second.
- **0**: Flush only when the log buffer is full (highest risk).

**Recommendation**: Use `1` for critical data and `2` for better performance with acceptable risk.
```ini
innodb_flush_log_at_trx_commit = 1
```

### File-Per-Table Option
Setting `innodb_file_per_table` creates a separate tablespace for each InnoDB table, improving manageability and performance.

**Recommendation**: Enable this setting:
```ini
innodb_file_per_table = 1
```

### Other Storage Engines Overview
- **MyISAM**: Suitable for read-heavy workloads but lacks transactional support.
- **Aria**: A crash-safe alternative to MyISAM, designed for temporary tables.

---

## Performance Optimization

### Query Cache Configuration

#### Enabling/Disabling Query Cache
The query cache stores the results of SELECT statements to improve read performance. However, it can slow down write-heavy workloads.

**Recommendation**: Disable query cache for write-heavy applications.
```ini
query_cache_type = 0
query_cache_size = 0
```

#### Sizing the Query Cache
For read-heavy workloads, allocate a small amount of memory to the query cache (e.g., 128M):
```ini
query_cache_size = 128M
```

### Temporary Table Settings

#### `tmp_table_size` and `max_heap_table_size`
These parameters control the maximum size of in-memory temporary tables. Larger values reduce the need for disk-based temporary tables.

**Recommendation**:
```ini
tmp_table_size = 128M
max_heap_table_size = 128M
```

### Thread and Connection Handling

#### `max_connections`
Defines the maximum number of simultaneous connections. Setting this too high can lead to resource exhaustion.

**Recommendation**: Adjust based on workload:
```ini
max_connections = 200
```

#### `thread_cache_size`
Controls the number of threads cached for reuse. Increasing this value reduces thread creation overhead.

**Recommendation**:
```ini
thread_cache_size = 100
```

### Buffer Pool Instances

#### Partitioning the Buffer Pool
Dividing the buffer pool into multiple instances can improve concurrency on large systems. 

**Recommendation**: Use one instance per GB of buffer pool size:
```ini
innodb_buffer_pool_instances = 6
```

---

## Logging and Monitoring

### Slow Query Logs

#### Enabling and Configuring Slow Query Logs
The slow query log captures queries that take longer than a specified threshold to execute.

**Recommendation**: Enable slow query logging:
```ini
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
```

#### `long_query_time` Threshold
Defines the time (in seconds) after which a query is considered slow.

**Recommendation**: Set based on your application requirements:
```ini
long_query_time = 2
```

### Log Verbosity Options
Increase the level of detail in logs to include query plans and InnoDB metrics:
```ini
log_slow_verbosity = query_plan,innodb,explain
```

### Monitoring Tools
Use tools like `mysqltuner` to analyze and optimize your MariaDB setup.

**Example**:
```bash
mysqltuner
```

---

## I/O and Disk Configuration

### I/O Capacity Settings (innodb_io_capacity, innodb_io_capacity_max)
The I/O capacity settings control the number of input/output operations per second (IOPS) that InnoDB can perform. These settings are crucial for optimizing disk performance, especially on systems with high I/O demands.

- **`innodb_io_capacity`**: Determines the rate at which background tasks, such as flushing dirty pages and merging inserts into indexes, are performed.
- **`innodb_io_capacity_max`**: Specifies the maximum IOPS for InnoDB tasks during peak load.

**Recommendations**:
- For SSDs, set `innodb_io_capacity` between `2000-10000` and `innodb_io_capacity_max` to around `20000`.
- For HDDs, set lower values, e.g., `200-500` for `innodb_io_capacity`.

**Example**:
```ini
innodb_io_capacity = 4000
innodb_io_capacity_max = 10000
```

### Swappiness and Kernel Settings
Swappiness determines how aggressively the Linux kernel swaps memory pages to disk. Reducing swappiness minimizes disk I/O caused by swapping, improving database performance.

**Recommendations**:
- Set `vm.swappiness` to `1` to prioritize keeping data in RAM.
- Ensure sufficient free memory to avoid excessive swapping.

**Steps**:
1. Check the current swappiness value:
   ```bash
   cat /proc/sys/vm/swappiness
   ```
2. Set swappiness to 1 temporarily:
   ```bash
   sudo sysctl vm.swappiness=1
   ```
3. Make the change permanent by adding the following to `/etc/sysctl.conf`:
   ```
   vm.swappiness = 1
   ```

### File System and I/O Scheduler Recommendations
The choice of file system and I/O scheduler greatly impacts MariaDB's performance. Modern file systems and optimized schedulers are better suited for database workloads.

- **File System**: Use `ext4` or `xfs` for SSDs and `ext4` for HDDs.
- **I/O Scheduler**:
  - For SSDs, use `none` or `mq-deadline` to minimize latency.
  - For HDDs, use `cfq` (Completely Fair Queuing) or `mq-deadline` for balanced performance.

**Steps**:
1. Check the current I/O scheduler for your disk:
   ```bash
   cat /sys/block/<device>/queue/scheduler
   ```
2. Set the scheduler to `mq-deadline` temporarily:
   ```bash
   echo mq-deadline | sudo tee /sys/block/<device>/queue/scheduler
   ```
3. Make the change permanent by editing the GRUB configuration:
   - Open `/etc/default/grub` and add:
     ```
     GRUB_CMDLINE_LINUX="elevator=mq-deadline"
     ```
   - Update GRUB:
     ```bash
     sudo update-grub
     ```

**Example Configuration**:
```ini
[mysqld]
data_file_path = /mnt/data/mysql
tmpdir = /mnt/data/tmp
innodb_io_capacity = 4000
innodb_io_capacity_max = 10000
```

These optimizations ensure efficient I/O operations, reduce disk bottlenecks, and enhance overall performance.

---

## Advanced Settings

### Replication Configuration
Replication in MariaDB ensures data redundancy and scalability by copying data between servers.

#### Master-Slave and Multi-Master Replication
- **Master-Slave Replication**: The master server processes write operations while slaves replicate the data for read operations.
- **Multi-Master Replication**: Allows multiple servers to handle write operations, useful for high availability.

**Configuration**:
1. Enable binary logging on the master:
   ```ini
   [mysqld]
   log_bin = /var/log/mysql/mysql-bin.log
   server_id = 1
   ```
2. Configure the slave:
   ```ini
   [mysqld]
   server_id = 2
   replicate_do_db = mydatabase
   ```
3. Start replication with:
   ```sql
   CHANGE MASTER TO MASTER_HOST='master_ip', MASTER_USER='replica_user', MASTER_PASSWORD='password';
   START SLAVE;
   ```

#### Binlog Settings
- **`binlog_format`**: Set to `ROW` for detailed changes, ensuring consistency.
- **`expire_logs_days`**: Automatically deletes old logs after a set number of days.

**Example**:
```ini
binlog_format = ROW
expire_logs_days = 7
```

### Galera Cluster Configuration
Galera Cluster provides synchronous multi-master replication for high availability.

**Configuration**:
1. Install Galera:
   ```bash
   sudo apt install galera-4 mariadb-server
   ```
2. Configure the cluster in `my.cnf`:
   ```ini
   [mysqld]
   wsrep_on = ON
   wsrep_provider = /usr/lib/galera/libgalera_smm.so
   wsrep_cluster_name = "my_cluster"
   wsrep_cluster_address = "gcomm://node1,node2,node3"
   ```

### Security Best Practices

#### Encryption Options
- Enable SSL for secure connections:
  ```ini
  [mysqld]
  ssl_cert = /path/to/server-cert.pem
  ssl_key = /path/to/server-key.pem
  ssl_ca = /path/to/ca-cert.pem
  ```

#### User Privileges and Authentication
- Use the `mysql_native_password` plugin for authentication.
- Grant minimal privileges:
  ```sql
  GRANT SELECT, INSERT, UPDATE ON mydatabase.* TO 'user'@'localhost';
  ```

---

## OS and Hardware Considerations

### Optimizing for SSDs and HDDs
- Use **SSDs** for data directories to reduce latency and improve IOPS.
- For HDDs, optimize with a proper I/O scheduler like `mq-deadline`.

### Swappiness Settings
Minimize swapping for better database performance:
```bash
sudo sysctl vm.swappiness=1
```
Make it permanent in `/etc/sysctl.conf`:
```ini
vm.swappiness = 1
```

### CPU and Memory Optimization
- Use all CPU cores by enabling multi-threading.
- Allocate 70-80% of RAM to `innodb_buffer_pool_size`.

---

## Common Pitfalls and Troubleshooting

### Avoiding Query Cache Misconfigurations
The query cache can cause bottlenecks in write-heavy workloads. Disable it:
```ini
query_cache_type = 0
query_cache_size = 0
```

### Common Error Logs and Solutions
- Check the error log for issues:
  ```bash
  tail -f /var/log/mysql/error.log
  ```
- Common issues include insufficient file permissions and out-of-memory errors. Ensure proper ownership of data directories:
  ```bash
  sudo chown -R mysql:mysql /var/lib/mysql
  ```

### Handling High CPU or Memory Usage
- Use the `performance_schema` to identify slow queries:
  ```sql
  SELECT * FROM performance_schema.events_statements_summary_by_digest ORDER BY COUNT_STAR DESC;
  ```
- Adjust `max_connections` and `innodb_buffer_pool_size` to match server capabilities.

---

## Sample Configurations

### Small Server Setup (2 CPUs, 4 GB RAM)
This configuration is suitable for lightweight applications and small-scale workloads.

**Configuration**:
```ini
[mysqld]
# General Settings
user = mysql
port = 3306
socket = /var/lib/mysql/mysql.sock
datadir = /var/lib/mysql

# InnoDB Settings
innodb_buffer_pool_size = 2G
innodb_log_file_size = 512M
innodb_flush_log_at_trx_commit = 2
innodb_file_per_table = 1
innodb_flush_method = O_DIRECT

# Connection Settings
max_connections = 100
thread_cache_size = 50

# Query Cache Settings
query_cache_type = 0
query_cache_size = 0

# Logging Settings
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2

# Buffer Settings
tmp_table_size = 64M
max_heap_table_size = 64M
```

### Medium Server Setup (4 CPUs, 8 GB RAM)
Designed for moderate workloads, such as small web applications or e-commerce sites.

**Configuration**:
```ini
[mysqld]
# General Settings
user = mysql
port = 3306
socket = /var/lib/mysql/mysql.sock
datadir = /var/lib/mysql

# InnoDB Settings
innodb_buffer_pool_size = 6G
innodb_log_file_size = 1G
innodb_flush_log_at_trx_commit = 1
innodb_file_per_table = 1
innodb_flush_method = O_DIRECT

# Connection Settings
max_connections = 200
thread_cache_size = 100

# Query Cache Settings
query_cache_type = 0
query_cache_size = 0

# Logging Settings
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2

# Buffer Settings
tmp_table_size = 128M
max_heap_table_size = 128M
```

### Large Server Setup (8 CPUs, 16 GB RAM)
Suitable for larger workloads, such as high-traffic websites or analytics platforms.

**Configuration**:
```ini
[mysqld]
# General Settings
user = mysql
port = 3306
socket = /var/lib/mysql/mysql.sock
datadir = /var/lib/mysql

# InnoDB Settings
innodb_buffer_pool_size = 12G
innodb_log_file_size = 2G
innodb_flush_log_at_trx_commit = 1
innodb_file_per_table = 1
innodb_flush_method = O_DIRECT

# Connection Settings
max_connections = 400
thread_cache_size = 200

# Query Cache Settings
query_cache_type = 0
query_cache_size = 0

# Logging Settings
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2

# Buffer Settings
tmp_table_size = 256M
max_heap_table_size = 256M
```

### High-Performance Server Setup (16+ CPUs, 64 GB RAM)
Designed for enterprise-level workloads, such as data warehouses, large-scale e-commerce, or SaaS platforms.

**Configuration**:
```ini
[mysqld]
# General Settings
user = mysql
port = 3306
socket = /var/lib/mysql/mysql.sock
datadir = /var/lib/mysql

# InnoDB Settings
innodb_buffer_pool_size = 50G
innodb_log_file_size = 4G
innodb_flush_log_at_trx_commit = 1
innodb_file_per_table = 1
innodb_flush_method = O_DIRECT

# Connection Settings
max_connections = 800
thread_cache_size = 400

# Query Cache Settings
query_cache_type = 0
query_cache_size = 0

# Logging Settings
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2

# Buffer Settings
tmp_table_size = 512M
max_heap_table_size = 512M
```

---

## References  

### Official MariaDB Documentation  
1. [MariaDB Official Documentation](https://mariadb.com/kb/en/documentation/)  
   - Comprehensive resource for installation, configuration, and troubleshooting.  

2. [MariaDB Configuration Settings](https://mariadb.com/kb/en/server-system-variables/)  
   - Detailed explanations of server variables and their usage.  

3. [MariaDB Backup](https://mariadb.com/kb/en/mariabackup/)  
   - Guides on performing physical backups for MariaDB.  

### Third-Party Resources  
4. [DigitalOcean: MariaDB Tutorials](https://www.digitalocean.com/community/tags/mariadb/)  
   - Practical guides on MariaDB installation, replication, and configuration.  

5. [Percona Blog](https://www.percona.com/blog/)  
   - Articles and tips about performance tuning, replication, and high availability.  

6. [MariaDB Forums](https://mariadb.com/forums/)  
   - A place to ask questions, share knowledge, and discuss MariaDB-related topics.  

### Tools and Utilities  
7. [MySQLTuner](https://github.com/major/MySQLTuner-perl)  
   - A script for analyzing and optimizing MariaDB and MySQL database performance.  

8. [SysBench](https://github.com/akopytov/sysbench)  
   - Benchmarking tool for database performance and stress testing.

