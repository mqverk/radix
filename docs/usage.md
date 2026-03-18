# Usage Guide

This document provides examples and explanations for using Radix effectively.

## Initializing the Database

Before indexing files, initialize the Radix database:

```bash
radix init
```

This creates a `.radix` directory with the SQLite database.

## Indexing Files

To index files in a directory:

```bash
radix index /path/to/directory
```

### Watching for Changes

To automatically re-index files when they change:

```bash
radix index /path/to/directory --watch
```

## Searching the Index

To search for a term:

```bash
radix search "search term"
```

### JSON Output

For machine-readable output:

```bash
radix search "search term" --json
```

## Checking Database Health

To verify the database integrity:

```bash
radix doctor
```