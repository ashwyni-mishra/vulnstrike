import asyncio
import logging
from typing import Tuple

logger = logging.getLogger("vulnstrike")

async def run_command(command: str) -> Tuple[str, str, int]:
    """Runs a shell command asynchronously and returns stdout, stderr, and exit code."""
    logger.debug(f"Executing: {command}")
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode().strip(), stderr.decode().strip(), process.returncode
