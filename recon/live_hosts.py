import logging
import tempfile
import os
from typing import List
from utils.exec import run_command

logger = logging.getLogger("vulnstrike")

class LiveHostDetector:
    def __init__(self, subdomains: List[str]):
        self.subdomains = subdomains

    async def detect(self) -> List[str]:
        logger.info("Detecting live hosts...")
        if not self.subdomains:
            return []

        # Create temporary file for subdomains
        fd, temp_path = tempfile.mkstemp()
        with os.fdopen(fd, 'w') as f:
            f.write('\n'.join(self.subdomains))

        live_hosts = []
        stdout, _, code = await run_command(f"httpx -l {temp_path} -silent")
        if code == 0 and stdout:
            live_hosts = stdout.split('\n')
        else:
            logger.warning("httpx failed or not installed. Assuming 'http://' for all subdomains.")
            live_hosts = [f"http://{sub}" for sub in self.subdomains]

        os.remove(temp_path)
        logger.debug(f"Found {len(live_hosts)} live hosts.")
        return live_hosts
