#!/bin/python3

import sqlite3
from config import db_name

class cursor:
    def __init__(self):
        self.connection = sqlite3.connect(db_name) 
        self.cursor = self.connection.cursor()

    def __enter__(self): # Start transaction
        self.cursor.execute("BEGIN;")
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # End transaction
        if exc_type is None:
            self.cursor.execute("COMMIT;")
        else: # Exception will be raised
            self.cursor.execute("ROLLBACK;")
        self.connection.close()
