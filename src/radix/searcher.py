import json
from .database import Database

class Searcher:
    """
    Handles search queries against the SQLite FTS5 database.
    """

    def __init__(self, db: Database):
        self.db = db

    def search(self, query: str, json_output: bool = False):
        """
        Executes a search query and returns matching results.
        """
        results = self.db.query(
            """
            SELECT path, snippet(files, 1, '[', ']', '...', 64) as snippet
            FROM files
            WHERE files MATCH ?
            ORDER BY rank;
            """,
            (query,)
        )
        if json_output:
            return json.dumps([
                {"path": path, "snippet": snippet} for path, snippet in results
            ])
        return results