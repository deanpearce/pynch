import sqlite3
import json
from sqlite3 import Connection, Cursor

def create_web_pages_table(connection: Connection):
    cursor = connection.cursor()
    cursor.execute("""
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
    """)
    connection.commit()

def insert_web_page(connection: Connection, web_page: dict):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO web_pages (
            id, url, content, content_type, fetch_time, modified_time,
            prev_fetch_time, prev_modified_time, status, title, text, inlinks, outlinks
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        web_page['id'], web_page['url'], web_page['content'], web_page['content_type'],
        web_page['fetch_time'], web_page['modified_time'],
        web_page['prev_fetch_time'], web_page['prev_modified_time'],
        web_page['status'], web_page['title'], web_page['text'],
        json.dumps(web_page['inlinks']), json.dumps(web_page['outlinks'])
    ))
    connection.commit()

def update_web_page(connection: Connection, web_page: dict):
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE web_pages SET
            url = ?, content = ?, content_type = ?,
            fetch_time = ?, modified_time = ?,
            prev_fetch_time = ?, prev_modified_time = ?,
            status = ?, title = ?, text = ?,
            inlinks = ?, outlinks = ?
        WHERE id = ?;
    """, (
        web_page['url'], web_page['content'], web_page['content_type'],
        web_page['fetch_time'], web_page['modified_time'],
        web_page['prev_fetch_time'], web_page['prev_modified_time'],
        web_page['status'], web_page['title'], web_page['text'],
        json.dumps(web_page['inlinks']), json.dumps(web_page['outlinks']),
        web_page['id']
    ))
    connection.commit()

def fetch_web_page(connection: Connection, id: str) -> dict:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM web_pages WHERE id = ?;
    """, (id,))
    row = cursor.fetchone()

    if row:
        return {
            'id': row[0],
            'url': row[1],
            'content': row[2],
            'content_type': row[3],
            'fetch_time': row[4],
            'modified_time': row[5],
            'prev_fetch_time': row[6],
            'prev_modified_time': row[7],
            'status': row[8],
            'title': row[9],
            'text': row[10],
            'inlinks': json.loads(row[11]),
            'outlinks': json.loads(row[12])
        }
    return None

if __name__ == "__main__":
    connection = sqlite3.connect("nutch_crawl_db.sqlite")
    create_web_pages_table(connection)
    connection.close()