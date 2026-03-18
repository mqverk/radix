# FAQ

## What is Radix?

Radix is a lightweight, local-first command-line search engine that uses SQLite's FTS5 extension for full-text search.

## How does Radix handle large directories?

Radix is optimized for performance and uses incremental indexing to avoid re-indexing unchanged files.

## Can I exclude files from being indexed?

Yes, use the `.radixignore` file to specify patterns for files and directories to exclude.

## Does Radix support binary files?

No, Radix is designed for text files only.

## How do I check the health of the database?

Use the `radix doctor` command to verify the integrity of the database:
```bash
radix doctor
```