# Examples

This section provides practical examples of using Radix.

## Example 1: Basic Workflow

1. Initialize the database:
   ```bash
   radix init
   ```

2. Index files in a directory:
   ```bash
   radix index /path/to/directory
   ```

3. Search for a term:
   ```bash
   radix search "example query"
   ```

## Example 2: Watching for Changes

1. Index files and watch for changes:
   ```bash
   radix index /path/to/directory --watch
   ```

2. Modify a file in the directory and observe automatic re-indexing.

## Example 3: JSON Output

1. Search with JSON output:
   ```bash
   radix search "example query" --json
   ```

2. Pipe the output to `jq` for formatting:
   ```bash
   radix search "example query" --json | jq
   ```