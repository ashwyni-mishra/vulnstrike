# Installation Guide

This guide will help you set up **VulnStrike** on your local machine.

## Prerequisites

VulnStrike is built with Python 3.8+ and relies on several external Go-based security tools.

### 1. Python Environment

Ensure you have Python 3.8 or higher installed. It is recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Python Dependencies

Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

*Note: If you are using Python 3.13+, you might encounter issues with the `cgi` module. Ensure your libraries (like `aiohttp`) are up to date.*

### 3. External Tool Dependencies

VulnStrike automates several industry-standard tools. For the framework to work correctly, you **must** have these installed and added to your system's `PATH`.

| Tool | Purpose | Installation |
| :--- | :--- | :--- |
| **Subfinder** | Subdomain Enumeration | `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` |
| **Assetfinder** | Subdomain Enumeration | `go install github.com/tomnomnom/assetfinder@latest` |
| **httpx** | Live Host Detection | `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest` |
| **gau** | Endpoint Discovery | `go install github.com/lc/gau/v2/cmd/gau@latest` |
| **waybackurls** | Endpoint Discovery | `go install github.com/tomnomnom/waybackurls@latest` |
| **Nuclei** | Vulnerability Scanning | `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| **Nmap** | Port Scanning | [Download Nmap](https://nmap.org/download.html) |

### 4. Verify Installation

Run the help command to ensure the script is accessible:

```bash
python vulnstrike.py --help
```

If you see the help menu, you're ready to start striking vulnerabilities!
