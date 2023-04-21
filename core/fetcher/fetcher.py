import importlib
from typing import List

from .fetcher_interface import FetcherInterface
from ..crawldb.crawldb import CrawlDB
from ..crawldb.status_enums import DbStatus

class Fetcher:

    def __init__(self, config: object, db_path: str):
        self.config = config
        self.crawl_db = CrawlDB(db_path)

    def init(self):
        plugin_name = self.config['chain'][0]
        injector = self.load_fetcher(plugin_name).entrypoint(self.config)
        return injector

    def load_fetcher(self, plugin_name: str) -> FetcherInterface:
        module_name = f"plugins.fetch_{plugin_name}"
        print(module_name)
        try:
            module = importlib.import_module(module_name)
            return module
        except ModuleNotFoundError:
            print(f"Error: Module {module_name} not found")
            return None