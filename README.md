# Radix

Radix is a lightweight, local-first command-line search engine designed for developers who value simplicity and performance. It leverages SQLite's FTS5 extension for high-performance full-text search without relying on external servers or containers.

## Philosophy

Radix was built to provide a fast, reliable, and local alternative to heavyweight search solutions like Elasticsearch. By focusing on SQLite and Python, Radix ensures minimal dependencies and maximum portability.

## Architecture

Radix uses a modular architecture:

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

## Why Not Elasticsearch?

- **No External Servers**: Radix runs entirely locally.
- **Lightweight**: No Docker, no JVM, no hassle.
- **Portable**: Works anywhere SQLite works.

## Usage

### Initialize
```bash
radix init
```

### Index Files
```bash
radix index /path/to/files
```

### Search
```bash
radix search "query"
```

### Watch for Changes
```bash
radix index /path/to/files --watch
```

### Check Database Health
```bash
radix doctor
```