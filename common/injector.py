from typing import List

from .crawldb.crawldb import CrawlDB
from .crawldb.status_enums import DbStatus

class Injector:

    def __init__(self, db_path: str):
        self.crawl_db = CrawlDB(db_path)

    @staticmethod
    def load_urls(file_path: str) -> List[str]:
        urls = []
        with open(file_path, "r") as f:
            for line in f:
                url = line.strip()
                if url:
                    urls.append(url)
        return urls

    def insert_urls(self, urls: List[str]):
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
