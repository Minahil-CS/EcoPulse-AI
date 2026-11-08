# EcoPulse AI – Setup & Local Mock Testing Guide

## Prerequisites
* Python 3.11 or higher
* Docker Desktop (for local containerized testing)
* Git

## Local Testing Steps

### 1. Mock Environment Setup
To test EcoPulse AI logic without a physical UGREEN NAS device:

```bash
# Clone the repository
git clone [https://github.com/Minahil-CS/EcoPulse-AI.git](https://github.com/Minahil-CS/EcoPulse-AI.git)
cd EcoPulse-AI

# Create a local test directory
mkdir -p mock_nas/data mock_nas/reports

# Generate mock files for lifecycle scanning
touch mock_nas/data/sample_doc.pdf