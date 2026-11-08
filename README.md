# 🌿 EcoPulse AI – Autonomous Energy & Storage Intelligence Copilot

[![UGOS Compatible](https://img.shields.io/badge/Target_OS-UGOS_v1.0-brightgreen.svg)](https://www.ugreen.com/)
[![Standard](https://img.shields.io/badge/Standard-Uliya_Skill_v1.0-blue.svg)](https://ugreenhackathon.devpost.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Privacy](https://img.shields.io/badge/Privacy-100%25_On--Device-orange.svg)](#)

> **EcoPulse AI** is a privacy-first, zero-cloud system skill engineered for UGREEN UGOS. It bridges local hardware telemetry with intelligent file lifecycle governance to eliminate storage redundancy, optimize disk thermal cycles, and dynamically defer compute-heavy AI tasks to eco-efficient runtime windows.

---

## 🏗️ System Architecture & Data Pipeline

EcoPulse AI operates natively within the UGOS environment, interacting directly with system event listeners without sending sensitive user telemetry or file indexes to third-party cloud services.
+-----------------------------------------------------------------------------------+
|                                 UGREEN UGOS Host                                  |
|                                                                                   |
|  +-----------------------+     +------------------------+     +----------------+  |
|  |  Drive Telemetry      |     | File System Event      |     | Storage Volume |  |
|  |  (Sysfs / Thermal)    |     | Hooks (Inotify)        |     | Manager        |  |
|  +-----------+-----------+     +-----------+------------+     +-------+--------+  |
+--------------|-----------------------------|--------------------------|-----------+
|                             |                          |

v                             v                          v

+-----------------------------------------------------------------------------------+
|                              EcoPulse AI Core Engine                              |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | 1. System Listener & Thermal Aggregator                                     |  |
|  +-----------------------------------------------------------------------------+  |
|  | 2. File Lifecycle & Deduplication Inspector (SHA-256 / Decay Heuristics)   |  |
|  +-----------------------------------------------------------------------------+  |
|  | 3. Dynamic Green Task Scheduler (Thermal Deferral Engine)                  |  |
|  +-----------------------------------------------------------------------------+  |
|  | 4. On-Device Report Generator                                               |  |
|  +-----------------------------------------------------------------------------+  |
+------------------------------------+----------------------------------------------+
|
v
+-----------------------------------------------------------------------------------+
|                        Local Output & Action Plan                                 |
|                  (/mock_nas/reports/eco_scorecard.md)                             |
+-----------------------------------------------------------------------------------+


---

## 🔬 Mathematical Models & Heuristics

EcoPulse AI employs two deterministic scoring engines to regulate background compute workload execution and cold storage tiering.

### 1. Thermal Stress & Deferral Score ($T_{stress}$)
To prevent local AI workloads (e.g., embedding generation, OCR indexing) from accelerating hardware degradation during elevated thermal cycles:

$$T_{stress} = \alpha \cdot \left(\frac{T_{current}}{T_{max}}\right) + \beta \cdot \left(\frac{IOPS_{active}}{IOPS_{peak}}\right)$$

* **Execution Rule:** If $T_{stress} > \text{Threshold}$, non-critical background AI tasks are deferred to idle runtime queues.

### 2. Storage Decay Score ($S_{decay}$)
Identifies stale media assets and unindexed temporary files for targeted local compression or disk spin-down:

$$S_{decay} = \frac{\Delta t_{idle} \times \text{Size}_{bytes}}{\log_{10}(\text{Access Count} + 1)}$$

---

## ⚡ Key Technical Innovations

* **Zero-Cloud Architecture:** Operates 100% offline within containerized UGOS environments using native Python routines and ONNX runtime wrappers.
* **Smart Spin-Down Optimization:** Reduces mechanical hard drive duty cycles by identifying cold storage blocks and suppressing unnecessary disk spin-up events.
* **Deterministic Deduplication:** Implements chunked SHA-256 digest hashing to safely flag duplicate media without altering file permissions or system stability.
* **Standard-Compliant Manifest:** Built following the official **Uliya Skill Development Standard** featuring strict JSON input/output event schemas.

---

## 📁 Repository Structure

```text
EcoPulse-AI/
├── SKILL.md                # Primary Uliya Skill specification manifest
├── main.py                 # Core functional engine & local simulation script
├── README.md               # Developer documentation & system specs
├── mock_nas/               # Local test environment container
│   ├── data/               # Target directory for storage scanning
│   └── reports/            # Output folder for generated Markdown scorecards
└── references/             # Technical specifications & JSON schemas
    ├── architecture.md     # In-depth module workflow & system permission model
    ├── setup.md            # Comprehensive setup & test execution guide
    └── api_reference.md    # Input/Output JSON schema definitions