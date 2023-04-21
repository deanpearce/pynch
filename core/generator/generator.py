from ..crawldb import CrawlDB

class Generator:
    def __init__(self, crawl_db_path):
        self.crawldb = CrawlDB(crawl_db_path)

    def __iter__(self):
      yield from self.crawldb.unfetched_web_pages()