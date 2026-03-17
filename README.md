# VulnStrike

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/ashwyni-mishra/vulnstrike?style=social)](https://github.com/ashwyni-mishra/vulnstrike)

**VulnStrike** is a professional-grade Bug Bounty and Security Automation framework. It streamlines the entire process of security testing, from reconnaissance to proof-of-concept validation, delivering comprehensive Markdown reports for security researchers and teams.

---

## 🚀 Key Features

*   **Comprehensive Recon**: Subdomain enumeration and live host detection.
*   **Deep Fingerprinting**: Identifying web stacks, frameworks, and CMS.
*   **CVE Intelligence**: Automated mapping of technologies to known CVEs.
*   **Vulnerability Scanning**: Integration with high-performance scanners like Nuclei.
*   **POC Validation**: Safe and automated verification of common web flaws.
*   **Professional Reporting**: Generates ready-to-deliver Markdown reports.

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

# Run your first assessment
python vulnstrike.py --target example.com
```

---

## ⚠️ Ethical Disclaimer

VulnStrike is intended for **authorized security testing and educational purposes only**. Using this tool against targets without prior written consent is illegal. The author is not responsible for any misuse or damage caused by this program.

---

## 👨‍💻 Author

**Ashwani Mishra (syn9)**
*   GitHub: [@ashwyni-mishra](https://github.com/ashwyni-mishra)
*   Twitter/X: [@syn9_sec](https://twitter.com/syn9_sec)

---

### Give it a Star! ⭐
If you find VulnStrike useful, please consider giving the repository a star to support the project!
