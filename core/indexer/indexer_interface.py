from typing import List
from ..crawldb import DbRecord

class IndexerResult:
    pass

class IndexerInterface:
    def index(self, document: List[DbRecord]) -> IndexerResult:
        """Method to index a document."""
        pass
