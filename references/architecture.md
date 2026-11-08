# EcoPulse AI – System Architecture & Technical Specifications

## 1. Core Modules

### Telemetry & Thermal Engine (`telemetry_engine`)
* Reads `/sys/class/hwmon` and UGOS storage CLI counters to collect drive temperatures, CPU load, and active read/write IOPS.
* Calculates host thermal stress scores ($T_{stress}$) to prevent background AI tasks from running during high thermal windows.

### Data Lifecycle Manager (`lifecycle_manager`)
* Performs asynchronous traversal of designated user directories.
* Computes file age decay scores ($S_{decay}$) using access time ($T_{access}$), file size ($S_{bytes}$), and duplicate hash matching ($H_{sha256}$).
* Outputs recommended actions: `SPIN_DOWN_DRIVE`, `COMPRESS_DIRECTORY`, or `MIGRATE_COLD_TIER`.

### Green Task Scheduler (`green_scheduler`)
* Evaluates pending background workloads (e.g., photo indexing, local vector generation).
* Applies execution rules based on thermal state and system idle thresholds:
  $$\text{Execution Condition} = (T_{stress} < T_{threshold}) \land (\text{System\_State} == \text{IDLE})$$

---

## 2. Security & Permission Model

EcoPulse AI operates under strict host isolation constraints:
* **Storage Access:** Read-only access to user data volumes; write access restricted to `/reports` and log directories.
* **Network Isolation:** Zero external network egress required. Works fully offline.
* **Privilege Level:** Non-root runtime container adhering to standard UGOS Skill security specifications.