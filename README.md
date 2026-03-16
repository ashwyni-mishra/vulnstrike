# VulnStrike

VulnStrike is a professional bug bounty automation framework. It automates reconnaissance, attack surface discovery, technology fingerprinting, CVE intelligence, vulnerability scanning, proof-of-concept validation, and Markdown reporting.

## Features
- **Reconnaissance**: Subdomain enumeration (Subfinder, Assetfinder) and live host detection (httpx).
- **Fingerprinting**: Identifies technologies, web servers, and frameworks.
- **Attack Surface**: Endpoint discovery via gau, waybackurls.
- **Vulnerability Scanning & POC**: Safe verification of XSS, missing headers, etc.
- **CVE Intelligence**: Maps detected tech to known CVEs.
- **Markdown Reporting**: Generates a professional security report.

## Installation
```bash
pip install -r requirements.txt
```
*Note: Make sure external tools like `subfinder`, `assetfinder`, `httpx`, `gau`, `waybackurls`, `nuclei`, and `nmap` are installed and in your PATH.*

## Usage
```bash
python vulnstrike.py --target example.com --mode full --threads 10 --report report.md --verbose
```

## Ethical Disclaimer
VulnStrike must only be used on systems where the user has authorization to perform security testing. Do not use for malicious purposes.

## Author
Created by syn9 (Ashwani Mishra)
GitHub: [https://github.com/ashwyni-mishra/vulnstrike](https://github.com/ashwyni-mishra/vulnstrike)
