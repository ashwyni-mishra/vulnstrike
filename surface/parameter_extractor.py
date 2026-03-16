import logging
from urllib.parse import urlparse, parse_qs

logger = logging.getLogger("vulnstrike")

class ParameterExtractor:
    def __init__(self, urls):
        self.urls = urls
        
    def extract(self):
        logger.info("Extracting parameters from URLs...")
        params = set()
        for url in self.urls:
            parsed = urlparse(url)
            query = parse_qs(parsed.query)
            for param in query.keys():
                params.add(param)
        return list(params)
