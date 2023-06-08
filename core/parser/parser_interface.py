from ..crawldb import DbRecord

class ParserInterface:
    def parse(self, document: DbRecord):
        """Method to parse a document."""
        pass
