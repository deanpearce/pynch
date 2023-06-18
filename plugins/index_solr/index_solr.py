from bs4 import BeautifulSoup, Tag
from typing import List, Dict, Any

from core.crawldb import DbRecord
from core.indexer import IndexerInterface, IndexerResult

class SolrIndexer(IndexerInterface):

    def __init__(self, config):
        pass

    def index(self, doc: List[DbRecord]) -> IndexerResult:

        result = IndexerResult()

        return result


if __name__ == "__main__":
    indexer = SolrIndexer()
    result = indexer.index([])