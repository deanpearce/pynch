import importlib
from typing import List

from .parser_interface import ParserInterface
from ..crawldb import CrawlDB, DbStatus

class Parser:

    def __init__(self, config: object, crawl_db: CrawlDB):
        self.config = config
        self.crawl_db = crawl_db

    def init(self) -> ParserInterface:
        plugin_name = self.config['chain'][0]
        parser = self.load_parser(plugin_name).entrypoint(self.config)
        return parser

    def load_parser(self, plugin_name: str) -> ParserInterface:
        module_name = f"plugins.parse_{plugin_name}"
        print(module_name)
        try:
            module = importlib.import_module(module_name)
            return module
        except ModuleNotFoundError:
            print(f"Error: Module {module_name} not found")
            return None