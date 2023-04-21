from .commondb import CommonDB

class CrawlDB(CommonDB):
    pass

if __name__ == "__main__":
    crawldb = CrawlDB("pynch_crawl_db.sqlite")
    crawldb.create_web_pages_table()
    crawldb.close()