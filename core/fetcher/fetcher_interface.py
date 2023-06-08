from ..crawldb import DbRecord

class FetcherInterface:
    def fetch(self, url: str) -> DbRecord:
        """Method to fetch a document from a source."""
        pass
