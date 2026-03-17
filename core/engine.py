import logging
from rich.progress import Progress
from recon.subdomains import SubdomainEnumerator
from recon.live_hosts import LiveHostDetector
from fingerprint.tech_detect import TechDetector
from surface.endpoint_discovery import EndpointDiscoverer
from intel.cve_lookup import CVELookup
from scanning.vuln_scan import VulnScanner
from exploit.poc_tests import POCTester
from reporting.pdf_report import PDFReportGenerator

logger = logging.getLogger("vulnstrike")

class Engine:
    def __init__(self, target: str, mode: str, threads: int, report_file: str, verbose: bool):
        self.target = target
        self.mode = mode
        self.threads = threads
        self.report_file = report_file
        self.verbose = verbose
        self.state = {
            "target": self.target,
            "subdomains": [],
            "live_hosts": [],
            "technologies": [],
            "endpoints": [],
            "cves": [],
            "vulnerabilities": []
        }

    async def run(self):
        logger.info(f"Starting VulnStrike on target: {self.target} in {self.mode} mode.")
        
        with Progress() as progress:
            if self.mode in ["recon", "full"]:
                task_recon = progress.add_task("[cyan]Reconnaissance...", total=2)
                
                # Subdomains
                sub_enum = SubdomainEnumerator(self.target)
                self.state["subdomains"] = await sub_enum.enumerate()
                progress.advance(task_recon)
                
                # Live Hosts
                live_detector = LiveHostDetector(self.state["subdomains"])
                self.state["live_hosts"] = await live_detector.detect()
                progress.advance(task_recon)

            if self.mode in ["scan", "full"]:
                task_scan = progress.add_task("[magenta]Scanning & Fingerprinting...", total=4)
                
                # Tech Fingerprinting
                tech_detector = TechDetector(self.state["live_hosts"])
                self.state["technologies"] = await tech_detector.detect()
                progress.advance(task_scan)
                
                # Surface Mapping
                surface_mapper = EndpointDiscoverer(self.target, self.state["live_hosts"])
                self.state["endpoints"] = await surface_mapper.discover()
                progress.advance(task_scan)
                
                # CVE Lookup
                cve_lookup = CVELookup(self.state["technologies"])
                self.state["cves"] = await cve_lookup.lookup()
                progress.advance(task_scan)
                
                # Vuln Scan
                vuln_scanner = VulnScanner(self.state["live_hosts"])
                self.state["vulnerabilities"].extend(await vuln_scanner.scan())
                progress.advance(task_scan)
                
            if self.mode in ["exploit", "full"]:
                task_exploit = progress.add_task("[red]POC Validation...", total=1)
                
                # POC Testing
                poc_tester = POCTester(self.state["endpoints"])
                self.state["vulnerabilities"].extend(await poc_tester.test())
                progress.advance(task_exploit)

        # Generate Report
        logger.info(f"Generating report at {self.report_file}")
        reporter = PDFReportGenerator(self.state, self.report_file)
        reporter.generate()
        logger.info("VulnStrike completed successfully.")
