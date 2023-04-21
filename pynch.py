from core.config import ConfigLoader
from core.injector import Injector
from core.generator import Generator
from core.fetcher import Fetcher


config = ConfigLoader("config/common.yaml")

db_path = config.get_global()['crawl_db']['path']
print(db_path)

def inject(db_path):
  injector = Injector(config.get_stage('inject'), db_path)
  urls = injector.init().load_urls()
  injector.inject(urls)

  del injector

def generate(db_path):
  generator = Generator(db_path)
  for record in generator:
    print(record['url'])
    fetch(record['url'])

def fetch(url):
  fetcher = Fetcher(config.get_stage('fetch'), db_path)
  contents = fetcher.init().fetch(url)
  print(contents)

inject(db_path)
generate(db_path)