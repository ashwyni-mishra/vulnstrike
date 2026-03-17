# Usage Guide

This guide details how to use **VulnStrike** to perform security assessments.

## Basic Command Syntax

```bash
python vulnstrike.py --target [DOMAIN] [OPTIONS]
```

## Mandatory Argument

*   `--target`: The base domain you wish to assess (e.g., `example.com`).

## Core Modes (`--mode`)

VulnStrike supports four modes of operation, allowing you to choose the level of assessment.

| Mode | Description |
| :--- | :--- |
| **recon** | Enumerates subdomains and identifies live hosts. |
| **scan** | Performs tech fingerprinting, CVE intelligence mapping, and vulnerability scanning. |
| **exploit** | Runs safe Proof-of-Concept (POC) validation on discovered endpoints. |
| **full** | (Default) Runs all stages sequentially from recon to exploitation. |

## Optional Flags

| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads` | Number of concurrent threads for faster processing. | `10` |
| `--report` | Custom path for the Markdown report output. | `report.md` |
| `--verbose` | Enable detailed output for debugging. | `False` |

---

## Example Usage Scenarios

### 1. Perform a Full Automated Assessment

The most common way to run VulnStrike. It will discover subdomains, find live hosts, scan for vulnerabilities, and generate a final report.

```bash
python vulnstrike.py --target bugcrowd.com
```

### 2. Recon Mode Only

Use this when you just want a list of subdomains and their live status without scanning.

```bash
python vulnstrike.py --target example.com --mode recon --report recon_results.md
```

### 3. High-Speed Scanning

If you have a high-performance machine and a large target, you can increase the thread count.

```bash
python vulnstrike.py --target corp-target.com --threads 50 --verbose
```

### 4. Continuous Security Monitoring

You can automate VulnStrike runs via Cron or Scheduled Tasks, pointing the report to a shared directory.

```bash
python vulnstrike.py --target myapp.com --report ./reports/$(date +%F)_myapp.md
```

## Viewing Results

VulnStrike generates a professional, human-readable **Markdown report**. You can view it in any Markdown viewer, VS Code, or convert it to PDF.
