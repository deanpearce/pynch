import importlib
from typing import List

from .injector_interface import InjectorInterface
from ..crawldb import CrawlDB, DbStatus

class Injector:

    def __init__(self, config: object, db_path: str):
        self.config = config
        self.crawl_db = CrawlDB(db_path)

    def init(self):
        plugin_name = self.config['chain'][0]
        injector = self.load_injector(plugin_name).entrypoint(self.config)
        return injector

    def load_injector(self, plugin_name: str) -> InjectorInterface:
        module_name = f"plugins.inject_{plugin_name}"
        print(module_name)
        try:
            module = importlib.import_module(module_name)
            return module
        except ModuleNotFoundError:
            print(f"Error: Module {module_name} not found")
            return None

    def inject(self, urls: List[str]):
        for url in urls:
            web_page = {
                'id': url,
                'url': url,
                'content': None,
                'content_type': None,
                'fetch_time': None,
                'modified_time': None,
                'prev_fetch_time': None,
                'prev_modified_time': None,
                'status': DbStatus.UNFETCHED.value,
                'title': None,
                'text': None,
                'inlinks': [],
                'outlinks': []
            }
            self.crawl_db.insert_web_page(web_page)

if __name__ == "__main__":
    # python3 -m pynch.common common/injector.py
    db_path = "nutch_crawl_db.sqlite"  # Replace with the path to your crawl database

    injector = Injector(db_path)

    urls_file = "test_data/urls.txt"  # Replace with the path to your text file containing URLs
    urls = Injector.load_urls(urls_file)
    injector.insert_urls(urls)
    injector.close()


    print(f"Loaded {len(urls)} URLs from {urls_file} and inserted them into the crawl database.")
