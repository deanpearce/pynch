from ..crawldb import CrawlDB

class Generator:
    def __init__(self, crawl_db: CrawlDB):
        self.crawl_db = crawl_db

    def __iter__(self):
      yield from self.crawl_db.unfetched_web_pages()