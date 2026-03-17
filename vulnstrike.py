#!/usr/bin/env python3
import argparse
import asyncio
import logging
import os
import re
from rich.console import Console
from rich.panel import Panel
from core.engine import Engine
from utils.logger import setup_logger

console = Console()

BANNER = """[bold red]
VulnStrike – Bug Bounty Automation Framework
Created by syn9
GitHub: https://github.com/ashwyni-mishra/vulnstrike
[/bold red]"""

DISCLAIMER = """[bold yellow]
ETHICAL DISCLAIMER: 
VulnStrike must only be used on systems where the user has authorization 
to perform security testing. Do not use for malicious purposes.
[/bold yellow]"""

def clean_target(target: str) -> str:
    # Remove http:// or https://
    target = re.sub(r'^https?://', '', target)
    # Remove any trailing paths or slashes
    target = target.split('/')[0]
    return target

def main():
    default_report = os.path.join(os.path.expanduser("~"), "report", "report.pdf")
    
    parser = argparse.ArgumentParser(description="VulnStrike - Bug Bounty Automation Framework")
    parser.add_argument("--target", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("--mode", choices=["recon", "scan", "exploit", "full"], default="full", help="Execution mode")
    parser.add_argument("--threads", type=int, default=10, help="Number of concurrent threads/tasks")
    parser.add_argument("--report", default=default_report, help=f"Output PDF report file (default: {default_report})")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose/debug output")

    args = parser.parse_args()
    
    # Sanitize the target input
    clean_domain = clean_target(args.target)

    # Expand any ~ in the report path if the user provided one
    args.report = os.path.expanduser(args.report)

    console.print(Panel(BANNER, expand=False))
    console.print(DISCLAIMER)

    logger = setup_logger(args.verbose)
    
    engine = Engine(
        target=clean_domain,
        mode=args.mode,
        threads=args.threads,
        report_file=args.report,
        verbose=args.verbose
    )
    
    try:
        asyncio.run(engine.run())
    except KeyboardInterrupt:
        logger.warning("Execution interrupted by user. Exiting...")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
