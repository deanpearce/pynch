import yaml

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as f:
            try:
                config_data = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(f"Error loading config file {self.config_path}: {exc}")
                return {}
        return config_data

    def get_global(self):
        return self.config_data['global']

    def get_stage(self, stage_name: str):
        return self.config_data['stages'][stage_name]