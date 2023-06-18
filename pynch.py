import logging
from typing import List
import core.logger

from core.crawldb import CrawlDB, DbRecord

from core.config import ConfigLoader
from core.injector import Injector
from core.generator import Generator
from core.fetcher import Fetcher
from core.parser import Parser

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

    records = []

    for record in generator:
        url = record['url']
        logging.debug(f"Fetching {url}")
        record = fetch_method.fetch(url)
        # print(record.content)
        records.append(record)

    parse(records)


def parse(docs: List[DbRecord]):
    logging.debug("Parsing URLs from crawl database")
    parser = Parser(config.get_stage('parse'), crawl_db)
    parser_method = parser.init()
    parser_method.parse(docs)

def index(docs: List[DbRecord]):
    pass

def update():
    pass

def main():

    logging.info("Starting Pynch")

    inject()

    generator = generate()

    fetch(generator)

    # parse()

    index()

    update()


if __name__ == "__main__":
    main()
