import logging
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import List, Dict

logger = logging.getLogger("vulnstrike")

class TechDetector:
    def __init__(self, hosts: List[str]):
        self.hosts = hosts
        self.technologies = []

    async def _analyze_host(self, session: aiohttp.ClientSession, host: str):
        try:
            async with session.get(host, timeout=5, ssl=False) as response:
                headers = response.headers
                server = headers.get("Server", "Unknown")
                powered_by = headers.get("X-Powered-By", "")
                
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                meta_generator = soup.find('meta', attrs={'name': 'generator'})
                generator = meta_generator['content'] if meta_generator else ""
                
                detected = []
                if server != "Unknown":
                    detected.append(server)
                if powered_by:
                    detected.append(powered_by)
                if generator:
                    detected.append(generator)
                    
                if detected:
                    tech_str = " | ".join(detected)
                    self.technologies.append({"host": host, "tech": tech_str})
                    logger.debug(f"Detected tech on {host}: {tech_str}")
                    
        except Exception as e:
            logger.debug(f"Failed to analyze {host}: {e}")

    async def detect(self) -> List[Dict[str, str]]:
        logger.info("Fingerprinting technologies...")
        async with aiohttp.ClientSession() as session:
            tasks = [self._analyze_host(session, host) for host in self.hosts]
            await asyncio.gather(*tasks)
        return self.technologies
