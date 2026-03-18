# Technical Architecture

Radix is built on a modular architecture to ensure simplicity, maintainability, and performance. Below is a detailed breakdown of its components.

## Overview

```
+-------------------+
|      CLI         |
|  (Typer + Rich)  |
+-------------------+
         |
         v
+-------------------+
|   Searcher       |
|   (FTS5 Query)   |
+-------------------+
         |
         v
+-------------------+
|   Indexer        |
| (File Walker)    |
+-------------------+
         |
         v
+-------------------+
|   Database       |
|  (SQLite FTS5)   |
+-------------------+
```

## Components

### CLI
- Built using `Typer` for command-line interface.
- Uses `Rich` for beautiful terminal output.

### Database
- SQLite database with FTS5 extension.
- Stores file paths, content, and checksums.

### Indexer
- Recursively walks directories to index text files.
- Supports `.radixignore` for excluding files.
- Uses SHA256 checksums for incremental indexing.

### Searcher
- Executes full-text search queries using FTS5.
- Supports JSON output for integration with other tools.