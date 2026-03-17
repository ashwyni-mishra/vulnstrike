import logging
import os
from fpdf import FPDF
from datetime import datetime
from typing import Dict, Any

logger = logging.getLogger("vulnstrike")

class PDFReportGenerator(FPDF):
    def __init__(self, state: Dict[str, Any], report_path: str):
        super().__init__()
        self.state = state
        self.report_path = report_path
        self.set_author("VulnStrike Framework")
        self.set_title(f"Security Assessment - {self.state['target']}")

    def header(self):
        # Only add header if not on the first page
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 10, f"VulnStrike Scan Report: {self.state['target']}", 0, 0, "L")
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "R")
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, "CONFIDENTIAL - Authorized Use Only", 0, 0, "C")

    def add_title_page(self):
        self.add_page()
        self.set_font("Helvetica", "B", 28)
        self.ln(60)
        self.cell(0, 20, "VULNSTRIKE", ln=True, align="C")
        self.set_font("Helvetica", "B", 18)
        self.cell(0, 10, "Security Assessment Report", ln=True, align="C")
        self.ln(20)
        
        self.set_font("Helvetica", "", 14)
        self.cell(0, 10, f"Target: {self.state['target']}", ln=True, align="C")
        self.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align="C")
        self.cell(0, 10, f"Mode: {self.state.get('mode', 'Full Scan').capitalize()}", ln=True, align="C")
        
        self.set_y(-60)
        self.set_font("Helvetica", "I", 10)
        self.cell(0, 5, "Created by syn9", ln=True, align="C")
        self.cell(0, 5, "https://github.com/ashwyni-mishra/vulnstrike", ln=True, align="C")

    def add_summary_page(self):
        self.add_page()
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "1. Executive Summary", ln=True)
        self.ln(5)
        
        self.set_font("Helvetica", "", 12)
        summary_text = (
            f"This report contains the results of an automated security assessment performed on {self.state['target']}. "
            f"The scan included reconnaissance, technology fingerprinting, and vulnerability scanning."
        )
        self.multi_cell(0, 8, summary_text)
        self.ln(10)

        # Statistics Table
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, "Scan Statistics:", ln=True)
        
        stats = [
            ("Subdomains Discovered", len(self.state['subdomains'])),
            ("Live Hosts", len(self.state['live_hosts'])),
            ("Technologies Identified", len(self.state['technologies'])),
            ("Endpoints Mapped", len(self.state['endpoints'])),
            ("Total Vulnerabilities", len(self.state['vulnerabilities']))
        ]
        
        self.set_font("Helvetica", "", 11)
        for label, val in stats:
            self.cell(80, 10, label, border=1)
            self.cell(40, 10, str(val), border=1, ln=True, align="C")
        self.ln(10)

    def add_vulnerability_details(self):
        self.add_page()
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "2. Vulnerability Findings", ln=True)
        self.ln(5)

        if not self.state['vulnerabilities']:
            self.set_font("Helvetica", "I", 12)
            self.cell(0, 10, "No vulnerabilities were identified during this scan.", ln=True)
            return

        # Sort vulns by severity: High -> Medium -> Low -> Info
        severity_map = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}
        sorted_vulns = sorted(self.state['vulnerabilities'], key=lambda x: severity_map.get(x.get('severity', 'Info'), 5))

        for idx, vuln in enumerate(sorted_vulns, 1):
            severity = vuln.get('severity', 'Info')
            
            # Severity color coding
            if severity in ["Critical", "High"]:
                self.set_text_color(200, 0, 0)
            elif severity == "Medium":
                self.set_text_color(200, 100, 0)
            else:
                self.set_text_color(0, 0, 0)

            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 10, f"{idx}. [{severity}] {vuln.get('type', 'Unknown Vulnerability')}")
            self.set_text_color(0, 0, 0) # Reset color
            
            self.set_font("Helvetica", "B", 11)
            self.cell(30, 8, "Target Host:")
            self.set_font("Helvetica", "", 11)
            self.cell(0, 8, vuln.get('target', 'N/A'), ln=True)
            
            if 'description' in vuln:
                self.set_font("Helvetica", "B", 11)
                self.cell(0, 8, "Description:", ln=True)
                self.set_font("Helvetica", "", 11)
                self.multi_cell(0, 7, vuln['description'])

            if 'remediation' in vuln:
                self.set_font("Helvetica", "B", 11)
                self.cell(0, 8, "Remediation:", ln=True)
                self.set_font("Helvetica", "", 11)
                self.multi_cell(0, 7, vuln['remediation'])
            
            self.ln(5)
            self.line(self.get_x(), self.get_y(), self.get_x() + 190, self.get_y())
            self.ln(5)

    def add_tech_details(self):
        self.add_page()
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "3. Infrastructure & Intelligence", ln=True)
        self.ln(5)

        self.set_font("Helvetica", "B", 13)
        self.cell(0, 10, "3.1 Technologies Detected", ln=True)
        self.set_font("Helvetica", "", 11)
        if self.state['technologies']:
            for t in self.state['technologies']:
                self.cell(0, 8, f"- {t['tech']} discovered on {t['host']}", ln=True)
        else:
            self.cell(0, 8, "No specific technologies identified.", ln=True)
        self.ln(5)

        self.set_font("Helvetica", "B", 13)
        self.cell(0, 10, "3.2 CVE Intelligence Mapping", ln=True)
        self.set_font("Helvetica", "", 11)
        if self.state['cves']:
            for c in self.state['cves']:
                self.set_font("Helvetica", "B", 11)
                self.cell(0, 8, f"[*] {c['cve']} ({c['tech']})", ln=True)
                self.set_font("Helvetica", "", 11)
                self.multi_cell(0, 6, c['description'])
                self.ln(2)
        else:
            self.cell(0, 8, "No known CVEs mapped to detected technologies.", ln=True)

    def generate(self):
        try:
            os.makedirs(os.path.dirname(self.report_path), exist_ok=True)
            
            self.add_title_page()
            self.add_summary_page()
            self.add_vulnerability_details()
            self.add_tech_details()
            
            self.output(self.report_path)
            logger.info(f"Comprehensive report successfully written to {self.report_path}")
            
        except Exception as e:
            logger.error(f"Failed to generate comprehensive PDF report: {e}")
            import traceback
            logger.debug(traceback.format_exc())
