import logging
from utils.exec import run_command

logger = logging.getLogger("vulnstrike")

class PortScanner:
    def __init__(self, target):
        self.target = target
        
    async def scan(self):
        logger.info(f"Running nmap port scan on {self.target}...")
        stdout, _, code = await run_command(f"nmap -F {self.target}")
        return stdout if code == 0 else ""
