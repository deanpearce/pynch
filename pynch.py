from common.injector import Injector
from common.generator import Generator

# Load Plugins
from plugins.fetch_http.fetch_http import FetchHttp

db_path = "nutch_crawl_db.sqlite"  # Replace with the path to your crawl database

# Instantiate Plugins

# TODO Move to config file
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
fetcher = FetchHttp(user_agent)

def inject(db_path):
  injector = Injector(db_path)
  urls_file = "test_data/urls.txt"  # Replace with the path to your text file containing URLs
  urls = Injector.load_urls(urls_file)
  injector.insert_urls(urls)

  del injector

def generate(db_path):
  generator = Generator(db_path)
  for record in generator:
    print(record['url'])
    print(fetcher.fetch(record['url']))

inject(db_path)
generate(db_path)