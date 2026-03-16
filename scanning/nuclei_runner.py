import logging
from utils.exec import run_command

logger = logging.getLogger("vulnstrike")

class NucleiRunner:
    def __init__(self, target_list_file):
        self.target_list_file = target_list_file
        
    async def run(self):
        logger.info("Executing Nuclei...")
        stdout, _, code = await run_command(f"nuclei -l {self.target_list_file} -silent")
        return stdout if code == 0 else ""
