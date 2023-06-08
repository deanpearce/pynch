class DbRecord:
    def __init__(self, id=None, url=None, content=None, content_type=None,
                 fetch_time=None, modified_time=None, prev_fetch_time=None,
                 prev_modified_time=None, status=None, title=None, text=None,
                 inlinks=None, outlinks=None):
        self.id = id
        self.url = url
        self.content = content
        self.content_type = content_type
        self.fetch_time = fetch_time
        self.modified_time = modified_time
        self.prev_fetch_time = prev_fetch_time
        self.prev_modified_time = prev_modified_time
        self.status = status
        self.title = title
        self.text = text
        self.inlinks = inlinks
        self.outlinks = outlinks