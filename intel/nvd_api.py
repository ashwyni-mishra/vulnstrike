import logging
import aiohttp

logger = logging.getLogger("vulnstrike")

class NVDApi:
    def __init__(self):
        self.base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        
    async def search(self, keyword):
        logger.debug(f"Querying NVD API for {keyword}...")
        # Placeholder for real NVD API query
        return []
