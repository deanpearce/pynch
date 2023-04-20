import json
import os
from typing import List, Dict, Any


class ConfigLoader:

    def __init__(self, config_files: List[str]):
        self.config = {}
        self.load_configs(config_files)

    def load_configs(self, config_files: List[str]):
        for config_file in config_files:
            if os.path.isfile(config_file):
                with open(config_file, "r") as f:
                    config_data = json.load(f)
                    self._update_config(self.config, config_data)
            else:
                print(f"Warning: Config file '{config_file}' not found.")

    @staticmethod
    def _update_config(config: Dict[str, Any], new_config: Dict[str, Any]):
        for key, value in new_config.items():
            if key in config and isinstance(config[key], dict) and isinstance(value, dict):
                ConfigLoader._update_config(config[key], value)
            else:
                config[key] = value

    def get_config(self) -> Dict[str, Any]:
        return self.config


if __name__ == "__main__":
    config_files = ["config1.json", "config2.json", "config3.json"]
    config_loader = ConfigLoader(config_files)
    config = config_loader.get_config()

    print("Merged Config:")
    print(json.dumps(config, indent=2))
