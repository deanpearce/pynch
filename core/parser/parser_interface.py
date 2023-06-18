from typing import List
from ..crawldb import DbRecord

class ParserInterface:
    def parse(self, document: List[DbRecord]):
        """Method to parse a document."""
        pass
