# BlackBox

**A Python-based file security application focused on file integrity, data protection, and secure file management.**

BlackBox is a personal Python project being developed to explore practical file-security concepts through a modular application. It currently includes a file integrity module that uses SHA-256 hashing to calculate and compare file and folder fingerprints.

The project is being built incrementally, with an emphasis on readable code, reusable modules, and practical security concepts.

## Features

### Implemented

- **File hashing:** Calculate SHA-256 hashes for individual files.
- **Folder hashing:** Generate a combined hash from the files and their relative paths within a folder, including nested files.
- **Integrity verification:** Compare a calculated hash against an expected hash to help identify changes.
- **Memory-efficient processing:** Read files in chunks instead of loading entire files into memory.
- **Modular structure:** Keep integrity-related functionality separate from the main application.

### Planned

- **File encryption and decryption:** Protect files using password-based, authenticated encryption.
- **Secure vault:** Organize and manage protected files.
- **Password tools:** Generate strong passwords and evaluate password strength.
- **Activity history:** Record relevant application operations.
- **Graphical interface:** Build a user-friendly interface for managing the application's features.

## Technologies

- **Python** — Core application language
- **hashlib** — SHA-256 hashing
- **pathlib** — File and directory path handling

## Project Structure

```text
BlackBox/
├── integrity/
│   ├── __init__.py
│   └── checksum.py
├── BlackBox.py
├── README.md
└── .gitignore
```

The `integrity` package contains the hashing and integrity-checking functionality. `BlackBox.py` is the current application entry point.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Git (optional, for cloning the repository)

### Run the Current Prototype

1. Clone the repository:

   ```bash
   git clone https://github.com/ab1ram/BlackBox.git
   ```

2. Open the project directory:

   ```bash
   cd BlackBox
   ```

3. Run the application:

   ```bash
   python BlackBox.py
   ```

4. Enter the path of an existing file or folder when prompted.

**Note:** The current entry point is a development test script. Its command-line workflow is still being refined.

## How Integrity Checking Works

Blackbox uses SHA-256 to produce a fixed-length hash from file contents. Even a small change to a file will ordinarily produce a different hash.

For folders, the integrity module processes files in a consistent sorted order and incorporates their relative paths and content hashes into a combined hash.

Comparing a newly calculated hash with a previously recorded hash helps detect changes to file contents, file names, or the folder's file structure.

## Project Status

**In development.**

The initial focus is the file integrity module. Encryption, vault management, password tools, activity history, and the graphical interface are planned extensions.

This project is intended for learning and demonstration. It has not yet been validated as a production-grade security application.

## Goals

- Apply Python programming concepts to a practical project.
- Develop a modular and maintainable codebase.
- Explore file integrity and other security-related concepts.
- Expand the application through independently developed features.