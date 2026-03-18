# Advanced Usage

This section covers advanced features and configurations of Radix.

## Using `.radixignore`

The `.radixignore` file allows you to exclude specific files or directories from being indexed. Place this file in the root of your project and add patterns to ignore.

### Example
```
# Ignore temporary files
*.tmp
*.bak

# Ignore logs
*.log

# Ignore specific directories
node_modules/
venv/
```

## Incremental Indexing

Radix uses SHA256 checksums to avoid re-indexing unchanged files. This ensures efficient updates to the index.

## JSON Output

The `--json` flag for the `radix search` command allows you to integrate Radix with other tools by providing machine-readable output.

### Example
```bash
radix search "example query" --json | jq
```