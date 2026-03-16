import logging

logger = logging.getLogger("vulnstrike")

class RiskScorer:
    def __init__(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities
        
    def calculate_score(self):
        logger.debug("Calculating overall risk score...")
        score = 0
        for vuln in self.vulnerabilities:
            if vuln.get('severity') == 'High':
                score += 10
            elif vuln.get('severity') == 'Medium':
                score += 5
            elif vuln.get('severity') == 'Low':
                score += 1
        return score
