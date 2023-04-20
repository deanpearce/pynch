import sqlite3
import json
import time

class CrawlDB:

    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.create_web_pages_table()

    def __del__(self):
        self.conn.close()

    def create_web_pages_table(self):
        cursor = self.conn.cursor()
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
        self.conn.commit()

    def insert_web_page(self, web_page: dict):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO web_pages (
                id, url, content, content_type, fetch_time, modified_time,
                prev_fetch_time, prev_modified_time, status, title, text, inlinks, outlinks
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                url = excluded.url,
                content = excluded.content,
                content_type = excluded.content_type,
                fetch_time = excluded.fetch_time,
                modified_time = excluded.modified_time,
                prev_fetch_time = excluded.prev_fetch_time,
                prev_modified_time = excluded.prev_modified_time,
                status = excluded.status,
                title = excluded.title,
                text = excluded.text,
                inlinks = excluded.inlinks,
                outlinks = excluded.outlinks;
        """, (
            web_page['id'], web_page['url'], web_page['content'], web_page['content_type'],
            web_page['fetch_time'], web_page['modified_time'],
            web_page['prev_fetch_time'], web_page['prev_modified_time'],
            web_page['status'], web_page['title'], web_page['text'],
            json.dumps(web_page['inlinks']), json.dumps(web_page['outlinks'])
        ))
        self.conn.commit()

    def update_web_page(self,web_page: dict):
        cursor = self.conn.cursor()
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
        self.conn.commit()

    def fetch_web_page(self, id: str) -> dict:
        cursor = self.conn.cursor()
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

    def unfetched_web_pages(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, url, fetch_time FROM web_pages WHERE fetch_time IS NULL OR fetch_time <= ?;
        """, (int(time.time()),))

        for row in cursor.fetchall():
            yield {
                'id': row[0],
                'url': row[1],
                'fetch_time': row[2]
            }

if __name__ == "__main__":
    crawldb = CrawlDB("nutch_crawl_db.sqlite")
    crawldb.create_web_pages_table()
    crawldb.close()