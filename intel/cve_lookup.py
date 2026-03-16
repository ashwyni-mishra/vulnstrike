import logging
from typing import List, Dict

logger = logging.getLogger("vulnstrike")

class CVELookup:
    def __init__(self, technologies: List[Dict[str, str]]):
        self.technologies = technologies

    async def lookup(self) -> List[Dict[str, str]]:
        logger.info("Looking up CVEs for detected technologies...")
        cves = []
        for tech_info in self.technologies:
            tech_str = tech_info['tech'].lower()
            if 'apache' in tech_str and '2.4.49' in tech_str:
                cves.append({
                    "tech": tech_info['tech'],
                    "cve": "CVE-2021-41773",
                    "description": "Apache Path Traversal"
                })
            elif 'php 7.4' in tech_str:
                cves.append({
                    "tech": tech_info['tech'],
                    "cve": "CVE-2022-31626",
                    "description": "PHP PDO MySQL buffer overflow"
                })
                
        if not cves and self.technologies:
             cves.append({
                 "tech": self.technologies[0]['tech'],
                 "cve": "Generic CVE Check",
                 "description": "Run specific nuclei templates for deeper CVE mapping."
             })
        return cves
