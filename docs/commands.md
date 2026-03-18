# Command Reference

Radix provides several commands to manage and query your local search index. Below is a detailed reference for each command.

## `radix init`

Initializes the Radix database.

### Usage
```bash
radix init
```

### Description
Creates a `.radix` directory in the current folder and initializes the SQLite database.

---

## `radix index`

Indexes files in the specified directory.

### Usage
```bash
radix index <path> [--watch]
```

### Options
- `--watch`: Watches the directory for changes and re-indexes files automatically.

---

## `radix search`

Searches the index for the specified query.

### Usage
```bash
radix search <query> [--json]
```

### Options
- `--json`: Outputs results in JSON format.

---

## `radix status`

Displays the status of the Radix database.

### Usage
```bash
radix status
```

---

## `radix doctor`

Checks the health of the Radix database.

### Usage
```bash
radix doctor
```