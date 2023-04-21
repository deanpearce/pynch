from core.config import ConfigLoader
from core.injector import Injector
from core.generator import Generator
from core.fetcher import Fetcher

# load config
config = ConfigLoader("config/common.yaml")

# config items
db_path = config.get_global()['crawl_db']['path']

def inject(db_path):
  injector = Injector(config.get_stage('inject'), db_path)
  urls = injector.init().load_urls()
  injector.inject(urls)

  del injector

def generate(db_path):
  generator = Generator(db_path)
  return generator


def fetch(url):
    fetcher = Fetcher(config.get_stage('fetch'), db_path)
    contents = fetcher.init().fetch(url)
    print(contents)

def parse():
    pass

def index():
    pass

def update():
    pass

def main():
    inject(db_path)
    generator = generate(db_path)

    for record in generator:
        fetch(record['url'])

    parse()

    index()

    update()

if __name__ == "__main__":
    main()
