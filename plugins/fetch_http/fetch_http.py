import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from core.crawldb import DbRecord

class FetchHttp:

    def __init__(self, config):
        self.user_agent = config['plugins']['http']['user_agent']
        self.timeout = config['plugins']['http']['timeout']
        self.max_retries = config['plugins']['http']['max_retries']
        self.session = self._create_session(self.max_retries)

    def _create_session(self, max_retries):
        session = requests.Session()

        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=0.1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def fetch(self, url) -> DbRecord:
        print(f"Fetching {url}...")
        headers = {'User-Agent': self.user_agent}
        try:
            response = self.session.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            record = DbRecord(id=url, url=url, content=response.content, content_type=response.headers['Content-Type'],)

            return record
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None


if __name__ == "__main__":
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    fetcher = FetchHttp(user_agent)
    url = "https://example.com"
    content = fetcher.fetch(url)

    if content:
        print(content)
    else:
        print("Failed to fetch the content")
