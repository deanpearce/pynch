CREATE TABLE IF NOT EXISTS web_pages (
    id TEXT PRIMARY KEY,
    url TEXT,
    content BLOB,
    content_type TEXT,
    fetch_time INTEGER,
    modified_time INTEGER,
    prev_fetch_time INTEGER,
    prev_modified_time INTEGER,
    status INTEGER,
    title TEXT,
    text TEXT,
    inlinks TEXT,
    outlinks TEXT
);
