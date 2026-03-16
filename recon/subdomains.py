import logging
from typing import List
from utils.exec import run_command

logger = logging.getLogger("vulnstrike")

class SubdomainEnumerator:
    def __init__(self, target: str):
        self.target = target

    async def enumerate(self) -> List[str]:
        logger.info(f"Enumerating subdomains for {self.target}")
        subdomains = set()
        
        # Subfinder
        stdout, _, code = await run_command(f"subfinder -d {self.target} -silent")
        if code == 0 and stdout:
            subdomains.update(stdout.split('\n'))
            
        # Assetfinder
        stdout, _, code = await run_command(f"assetfinder --subs-only {self.target}")
        if code == 0 and stdout:
            subdomains.update(stdout.split('\n'))
            
        if not subdomains:
            logger.warning(f"No subdomains found for {self.target}. External tools may not be installed. Using target as sole host.")
            subdomains.add(self.target)
            
        logger.debug(f"Found {len(subdomains)} subdomains.")
        return list(subdomains)
