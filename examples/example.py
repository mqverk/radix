from pathlib import Path
from radix.database import Database
from radix.indexer import Indexer
from radix.searcher import Searcher

# Initialize the database
db_path = Path(".radix/index.db")
db = Database(db_path)
db.initialize()

# Index files
indexer = Indexer(db)
indexer.index_directory(Path("/path/to/directory"))

# Search the index
searcher = Searcher(db)
results = searcher.search("example query")

for path, snippet in results:
    print(f"{path}: {snippet}")