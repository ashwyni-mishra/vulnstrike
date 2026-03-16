#!/usr/bin/env python3
import argparse
import asyncio
import logging
from rich.console import Console
from rich.panel import Panel
from core.engine import Engine
from utils.logger import setup_logger

console = Console()

BANNER = """[bold red]
VulnStrike – Bug Bounty Automation Framework
Created by syn9 (Ashwani Mishra)
GitHub: https://github.com/ashwyni-mishra/vulnstrike
[/bold red]"""

DISCLAIMER = """[bold yellow]
ETHICAL DISCLAIMER: 
VulnStrike must only be used on systems where the user has authorization 
to perform security testing. Do not use for malicious purposes.
[/bold yellow]"""

def main():
    parser = argparse.ArgumentParser(description="VulnStrike - Bug Bounty Automation Framework")
    parser.add_argument("--target", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("--mode", choices=["recon", "scan", "exploit", "full"], default="full", help="Execution mode")
    parser.add_argument("--threads", type=int, default=10, help="Number of concurrent threads/tasks")
    parser.add_argument("--report", default="report.md", help="Output Markdown report file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose/debug output")

    args = parser.parse_args()

    console.print(Panel(BANNER, expand=False))
    console.print(DISCLAIMER)

    logger = setup_logger(args.verbose)
    
    engine = Engine(
        target=args.target,
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
