import importlib
from typing import List

from .indexer_interface import IndexerInterface
from ..crawldb import CrawlDB, DbStatus

class Indexer:

    def __init__(self, config: object, crawl_db: CrawlDB):
        self.config = config
        self.crawl_db = crawl_db

    def init(self) -> IndexerInterface:
        plugin_name = self.config['chain'][0]
        indexer = self.load_indexer(plugin_name).entrypoint(self.config)
        return indexer

    def load_indexer(self, plugin_name: str) -> IndexerInterface:
        module_name = f"plugins.index_{plugin_name}"
        print(module_name)
        try:
            module = importlib.import_module(module_name)
            return module
        except ModuleNotFoundError:
            print(f"Error: Module {module_name} not found")
            return None