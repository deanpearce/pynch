from enum import StrEnum, auto

class DbStatus(StrEnum):

    # page is not fetched yet
    UNFETCHED = auto()

    # page was successfully fetched
    FETCHED = auto()

    # page no longer exists
    GONE = auto()

    # page temporily redirects to another page
    REDIR_TEMPORARY = auto()

    # page permanently redirects to another page
    REDIR_PERMANENT = auto()

    # page was successfully fetched but not modified
    NOT_MODIFIED = auto()

    # page was marked as a duplicate of another page
    DUPLICATE = auto()

    # page was marked as an orphan (no inlinks)
    ORPHAN = auto()
