import os
import sqlite3

from datetime import datetime
from .commondb import CommonDB


class Segment(CommonDB):

    def __init__(self, config: dict):

        segment_path = config['crawldb']['segment_path']
        self.segment_name = self.create_segment_path(segment_path)
        self.conn = sqlite3.connect(self.segment_name)
        self.create_web_pages_table()

    def create_segment_path(segment_path: str):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Create the folder name
        folder_name = f"{segment_path}/segment_{timestamp}"

        # Create the folder
        os.mkdir(folder_name)

        # Return the folder name
        return folder_name

if __name__ == "__main__":
    segment = Segment("pynch_segment_db.sqlite")
    segment.create_web_pages_table()
    segment.close()