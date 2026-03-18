import sqlite3
from pathlib import Path

class Database:
    """
    Handles SQLite database operations, including initialization and connection management.
    """

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.connection = None

    def initialize(self):
        """
        Initializes the SQLite database with the required FTS5 table.
        """
        self.connection = sqlite3.connect(self.db_path)
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.connection.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS files USING fts5(
                path UNINDEXED,
                content,
                tokenize = 'porter'
            );
            """
        )
        self.connection.commit()

    def connect(self):
        """
        Establishes a connection to the SQLite database.
        """
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute(self, query: str, params: tuple = ()):  # type: ignore
        """
        Executes a query on the database.
        """
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def query(self, query: str, params: tuple = ()):  # type: ignore
        """
        Executes a SELECT query and returns the results.
        """
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()