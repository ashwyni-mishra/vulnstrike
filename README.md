# VulnStrike

```text
  _   _       _       _____ _        _ _        
 | | | |     | |     /  ___| |      (_) |       
 | | | |_   _| |_ __ \ `--.| |_ _ __ _| | _____ 
 | | | | | | | | '_ \ `--. \ __| '__| | |/ / _ \
 \ \_/ / |_| | | | | /\__/ / |_| |  | |   <  __/
  \___/ \__,_|_|_| |_\____/ \__|_|  |_|_|\_\___|
                                                
   Professional Bug Bounty Automation Framework
```

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

[![GitHub Stars](https://img.shields.io/github/stars/ashwyni-mishra/vulnstrike?style=social)](https://github.com/ashwyni-mishra/vulnstrike)

**VulnStrike** is a professional-grade Bug Bounty and Security Automation framework. It streamlines the entire process of security testing, from reconnaissance to proof-of-concept validation, delivering comprehensive PDF reports for security researchers and teams.

---

## 🚀 Key Features

*   **Comprehensive Recon**: Subdomain enumeration and live host detection.
*   **Deep Fingerprinting**: Identifying web stacks, frameworks, and CMS.
*   **CVE Intelligence**: Automated mapping of technologies to known CVEs.
*   **Vulnerability Scanning**: Integration with high-performance scanners like Nuclei.
*   **POC Validation**: Safe and automated verification of common web flaws.
*   **Professional PDF Reporting**: Generates ready-to-deliver, comprehensive security reports.

---

## 📖 Documentation

To keep things organized, we've split our documentation into specialized guides:

1.  **[🛠️ Installation Guide](./docs/INSTALLATION.md)**: How to set up VulnStrike and its external dependencies.
2.  **[💻 Usage & Commands](./docs/USAGE.md)**: Detailed CLI options, modes, and example workflows.
3.  **[🔍 Features Deep Dive](./docs/FEATURES.md)**: Learn how VulnStrike's modules work under the hood.

---

## ⚡ Quick Start

After [installing](./docs/INSTALLATION.md) the prerequisites:

```bash
# Clone the repository
git clone https://github.com/ashwyni-mishra/vulnstrike.git
cd vulnstrike

# Install Python requirements
pip install -r requirements.txt

# Run your first assessment (Report will be in ~/report/report.pdf)
python vulnstrike.py --target example.com
```

---

## ⚠️ Ethical Disclaimer

VulnStrike is intended for **authorized security testing and educational purposes only**. Using this tool against targets without prior written consent is illegal. The author is not responsible for any misuse or damage caused by this program.

---

## 👨‍💻 Author

**syn9**
*   GitHub: [https://github.com/ashwyni-mishra](https://github.com/ashwyni-mishra)

---

### Give it a Star! ⭐
If you find VulnStrike useful, please consider giving the repository a star to support the project!
