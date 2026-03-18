import os
from pathlib import Path
from .database import Database
import hashlib

class Indexer:
    """
    Handles file indexing into the SQLite FTS5 database.
    """

    def __init__(self, db: Database):
        self.db = db
        self.ignored_patterns = self.load_radixignore()

    def load_radixignore(self):
        """
        Loads patterns from the .radixignore file.
        """
        ignore_file = Path(".radixignore")
        if ignore_file.exists():
            with open(ignore_file, "r") as f:
                return [line.strip() for line in f if line.strip() and not line.startswith("#")]
        return []

    def should_ignore(self, file_path: Path) -> bool:
        """
        Checks if a file matches any ignore patterns.
        """
        for pattern in self.ignored_patterns:
            if file_path.match(pattern):
                return True
        return False

    def index_directory(self, directory: Path):
        """
        Recursively indexes all text files in the given directory.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = Path(root) / file
                if not self.should_ignore(file_path) and self.is_text_file(file_path):
                    self.index_file(file_path)

    def index_file(self, file_path: Path):
        """
        Reads and indexes the content of a single file, only if it has changed.
        """
        try:
            file_hash = self.calculate_file_hash(file_path)
            existing_hash = self.db.query(
                "SELECT checksum FROM files WHERE path = ?;",
                (str(file_path),),
            )
            if existing_hash and existing_hash[0][0] == file_hash:
                return  # Skip re-indexing unchanged files

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.db.execute(
                "INSERT OR REPLACE INTO files (path, content, checksum) VALUES (?, ?, ?);",
                (str(file_path), content, file_hash),
            )
        except Exception as e:
            print(f"Failed to index {file_path}: {e}")

    @staticmethod
    def is_text_file(file_path: Path) -> bool:
        """
        Determines if a file is a text file based on its extension.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                f.read(1024)  # Try reading a small chunk
            return True
        except Exception:
            return False

    @staticmethod
    def calculate_file_hash(file_path: Path) -> str:
        """
        Calculates the SHA256 hash of a file.
        """
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()