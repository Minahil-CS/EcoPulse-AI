"""
EcoPulse AI - Core Engine Prototype
Engineered for UGREEN UGOS Hackathon 2026
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime

class EcoPulseEngine:
    def __init__(self, target_dir="./mock_nas/data", report_dir="./mock_nas/reports"):
        self.target_dir = Path(target_dir)
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(parents=True, exist_ok=True)
        self.target_dir.mkdir(parents=True, exist_ok=True)

    def calculate_sha256(self, filepath):
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception:
            return None

    def analyze_storage(self):
        seen_hashes = {}
        duplicates = []
        total_size = 0

        for root, _, files in os.walk(self.target_dir):
            for file in files:
                filepath = Path(root) / file
                size = filepath.stat().st_size
                total_size += size

                file_hash = self.calculate_sha256(filepath)
                if file_hash:
                    if file_hash in seen_hashes:
                        duplicates.append((filepath, seen_hashes[file_hash]))
                    else:
                        seen_hashes[file_hash] = filepath

        return {
            "total_files": len(seen_hashes) + len(duplicates),
            "total_size_bytes": total_size,
            "duplicate_count": len(duplicates),
            "duplicates": duplicates
        }

    def generate_eco_scorecard(self, results):
        report_path = self.report_dir / "eco_scorecard.md"
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        saved_bytes = sum(f[0].stat().st_size for f in results["duplicates"]) if results["duplicates"] else 0
        saved_mb = round(saved_bytes / (1024 * 1024), 2)

        markdown_content = f"""# EcoPulse AI - UGOS Environmental Scorecard

**Generated at:** {now}

## System Overview
- **Storage Directory Analyzed:** `{self.target_dir}`
- **Total Scanned Files:** {results['total_files']}
- **Total Directory Size:** {round(results['total_size_bytes'] / (1024 * 1024), 2)} MB

## Sustainability Metrics
- **Duplicate Files Identified:** {results['duplicate_count']}
- **Potential Storage Recovered:** {saved_mb} MB
- **Recommended Action:** Execute background spin-down for idle media arrays.
- **Privacy Assurance:** 100% On-Device Analysis (Zero Cloud Transmission)
"""
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print("[+] EcoPulse AI Report generated successfully at:", report_path)

if __name__ == "__main__":
    engine = EcoPulseEngine()
    analysis_results = engine.analyze_storage()
    engine.generate_eco_scorecard(analysis_results)