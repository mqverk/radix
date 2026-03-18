import typer
from pathlib import Path
from rich.console import Console
from .database import Database
from .indexer import Indexer
from .searcher import Searcher
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Watcher:
    """
    Watches a directory for changes and triggers re-indexing.
    """

    def __init__(self, path: Path, indexer: Indexer):
        self.path = path
        self.indexer = indexer

    def start(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_event
        event_handler.on_created = self.on_event
        observer = Observer()
        observer.schedule(event_handler, str(self.path), recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def on_event(self, event):
        file_path = Path(event.src_path)
        if file_path.is_file():
            self.indexer.index_file(file_path)

app = typer.Typer()
console = Console()

def get_database() -> Database:
    """
    Returns a Database instance for the current directory.
    """
    db_path = Path(".radix") / "index.db"
    return Database(db_path)

@app.command()
def init():
    """
    Initializes the Radix database.
    """
    db_path = Path(".radix")
    db_path.mkdir(exist_ok=True)
    db = get_database()
    db.initialize()
    console.print("[green]Radix initialized successfully![/green]")

@app.command()
def index(path: Path, watch: bool = False):
    """
    Indexes files in the given directory. Optionally watches for changes.
    """
    db = get_database()
    indexer = Indexer(db)
    indexer.index_directory(path)
    console.print(f"[green]Indexed files in {path}[/green]")

    if watch:
        console.print("[yellow]Watching for changes... Press Ctrl+C to stop.[/yellow]")
        watcher = Watcher(path, indexer)
        watcher.start()

@app.command()
def search(query: str, json: bool = False):
    """
    Searches the index for the given query. Optionally outputs JSON.
    """
    db = get_database()
    searcher = Searcher(db)
    results = searcher.search(query, json_output=json)
    if json:
        console.print(results)
    else:
        for path, snippet in results:
            console.print(f"[blue]{path}[/blue]: {snippet}")

@app.command()
def doctor():
    """
    Checks the health of the Radix database.
    """
    db = get_database()
    try:
        db.query("SELECT 1 FROM files LIMIT 1;")
        console.print("[green]Database is healthy.[/green]")
    except Exception as e:
        console.print(f"[red]Database error: {e}[/red]")