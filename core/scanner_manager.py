import logging
import importlib
import os

logger = logging.getLogger("vulnstrike")

class ScannerManager:
    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = plugin_dir
        self.plugins = []

    def load_plugins(self):
        logger.info("Loading plugins...")
        if not os.path.exists(self.plugin_dir):
            return
            
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"{self.plugin_dir}.{filename[:-3]}"
                try:
                    module = importlib.import_module(module_name)
                    logger.debug(f"Loaded plugin: {module_name}")
                    # In a real scenario, instantiate and store the plugin classes here
                except Exception as e:
                    logger.error(f"Failed to load plugin {module_name}: {e}")
