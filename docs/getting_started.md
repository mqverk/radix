# Getting Started

This guide will help you set up and start using Radix.

## Installation

Ensure you have Python 3.10+ installed. Then, install Radix using pip:

```bash
pip install radix-cli
```

## Initialization

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

## Searching the Index

To search for a term:

```bash
radix search "search term"
```