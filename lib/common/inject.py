import sqlite3
from sqlite3 import Connection
from typing import List

from crawldb import create_web_pages_table, insert_web_page, DbStatus

def load_urls(file_path: str) -> List[str]:
    urls = []
    with open(file_path, "r") as f:
        for line in f:
            url = line.strip()
            if url:
                urls.append(url)
    return urls

def insert_urls(connection: Connection, urls: List[str]):
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
        insert_web_page(connection, web_page)

if __name__ == "__main__":
    connection = sqlite3.connect("nutch_crawl_db.sqlite")
    create_web_pages_table(connection)

    urls_file = "urls.txt"  # Replace with the path to your text file containing URLs
    urls = load_urls(urls_file)
    insert_urls(connection, urls)
    connection.close()

    print(f"Loaded {len(urls)} URLs from {urls_file} and inserted them into the crawl database.")
