import logging
import core.logger

from core.crawldb import CrawlDB

from core.config import ConfigLoader
from core.injector import Injector
from core.generator import Generator
from core.fetcher import Fetcher

# logging
core.logger.configure_logging("logs/pynch.log")

# load config
config = ConfigLoader("config/common.yaml")

crawl_db = CrawlDB(config.get_global())

def inject():
  logging.debug("Injecting URLs into crawl database")
  injector = Injector(config.get_stage('inject'), crawl_db)
  urls = injector.init().load_urls()
  injector.inject(urls)

  del injector

def generate():
  logging.debug("Generating URLs from crawl database")
  generator = Generator(crawl_db)
  return generator


def fetch(generator):
    logging.debug("Fetching URLs from crawl database")
    fetcher = Fetcher(config.get_stage('fetch'), crawl_db)
    fetch_method = fetcher.init()

    for record in generator:
        url = record['url']
        logging.debug(f"Fetching {url}")
        contents = fetch_method.fetch(url)
        print(contents)

def parse():
    pass

def index():
    pass

def update():
    pass

def main():

    logging.info("Starting Pynch")

    inject()

    generator = generate()

    fetch(generator)

    parse()

    index()

    update()


if __name__ == "__main__":
    main()
