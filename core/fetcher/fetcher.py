import importlib
from typing import List

from .fetcher_interface import FetcherInterface
from ..crawldb import CrawlDB, DbStatus

class Fetcher:

    def __init__(self, config: object, crawl_db: CrawlDB):
        self.config = config
        self.crawl_db = crawl_db

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