# Features and Core Modules

**VulnStrike** is a comprehensive framework that connects multiple security testing phases into one seamless workflow.

## 1. Reconnaissance (`recon/`)

The recon module is the foundation of every assessment. It focuses on finding every possible entry point for a given target.

*   **Subdomain Enumeration**: Integrates with `subfinder` and `assetfinder` to query public sources and discover subdomains.
*   **Live Host Detection**: Uses `httpx` to verify which subdomains are currently active, reducing noise in the later stages.

## 2. Fingerprinting (`fingerprint/`)

Understanding the target's stack is key to identifying specific vulnerabilities.

*   **Tech Detection**: Identifies the programming languages, web servers (Nginx, Apache), and CMS (WordPress, Joomla) being used.
*   **Port Scanning**: Optionally integrates with `nmap` to find open services beyond just HTTP/HTTPS.

## 3. Attack Surface Discovery (`surface/`)

Discovering where to attack is as important as how to attack.

*   **Endpoint Discovery**: Uses `gau` and `waybackurls` to pull historical and current endpoints for each live host.
*   **Parameter Extraction**: Automatically parses JavaScript files and HTML to find query parameters, headers, and hidden API endpoints.

## 4. CVE Intelligence (`intel/`)

Automatically maps discovered technologies to the latest known vulnerabilities.

*   **NVD/CVE Lookup**: Cross-references identified stacks with the National Vulnerability Database (NVD) to alert the user about outdated software and relevant CVEs.

## 5. Vulnerability Scanning (`scanning/`)

Uses powerful engines to find security flaws.

*   **Nuclei Integration**: Leverages thousands of community-curated templates for identifying misconfigurations, exposed panels, and critical CVEs.
*   **Custom Scanners**: Built-in logic for checking missing security headers, SSL/TLS issues, and common web weaknesses.

## 6. POC Validation (`exploit/`)

VulnStrike doesn't just report—it verifies (safely).

*   **POC Tests**: Executes non-intrusive tests to confirm vulnerabilities like Reflected XSS, Open Redirects, and insecure file exposures.
*   **Verification**: Only vulnerabilities that can be verified are prioritized in the final report, reducing false positives.

## 7. Professional Reporting (`reporting/`)

The end result of every assessment is a high-quality Markdown report.

*   **Categorized Results**: Vulnerabilities are grouped by severity (Critical, High, Medium, Low).
*   **Remediation**: Includes basic steps for fixing the identified issues.
*   **Evidence**: Links and findings are clearly listed for easy verification by security teams.
