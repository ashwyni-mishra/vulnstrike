import logging
from typing import List
from utils.exec import run_command

logger = logging.getLogger("vulnstrike")

class EndpointDiscoverer:
    def __init__(self, target: str, live_hosts: List[str]):
        self.target = target
        self.live_hosts = live_hosts

    async def discover(self) -> List[str]:
        logger.info("Discovering endpoints...")
        endpoints = set()
        
        # Waybackurls
        stdout, _, code = await run_command(f"echo {self.target} | waybackurls")
        if code == 0 and stdout:
            lines = stdout.split('\n')
            endpoints.update(lines[:100]) # Limit to prevent huge lists in memory
            
        # gau
        stdout, _, code = await run_command(f"gau {self.target}")
        if code == 0 and stdout:
            lines = stdout.split('\n')
            endpoints.update(lines[:100])
            
        logger.debug(f"Discovered {len(endpoints)} potential endpoints.")
        return list(endpoints)
