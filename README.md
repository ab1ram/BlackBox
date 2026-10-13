# BlackBox

**A Python-based file security application focused on file integrity, data protection, and secure file management.**

BlackBox is a personal Python project being developed to explore practical file-security concepts through a modular application. It currently includes a file integrity module that uses SHA-256 hashing to calculate and compare file and folder fingerprints, a password generator, and a basic rule-based password strength checker.

The project is being built incrementally, with an emphasis on readable code, reusable modules, and practical security concepts.

## Features

### Implemented

- **File hashing:** Calculate SHA-256 hashes for individual files.
- **Folder hashing:** Generate a combined hash from the files and their relative paths within a folder, including nested files.
- **Integrity verification:** Compare a calculated hash against an expected hash to help identify changes.
- **Memory-efficient processing:** Read files in chunks instead of loading entire files into memory.
- **Modular structure:** Keep integrity-related functionality separate from the main application.
- **Password generation:** Generate random passwords with configurable minimum character counts for uppercase letters, lowercase letters, digits, and symbols.
- **Password strength checker:** A basic rule-based password strength checker that evaluates passwords against five requirements:
  - Minimum length of 12 characters.
  - At least 2 uppercase letters.
  - At least 2 lowercase letters.
  - At least 2 digits.
  - At least 2 special characters.

  **Limitations:** This checker evaluates password length and character composition only. It does not detect common passwords, dictionary words, predictable patterns, or estimate resistance to password-guessing attacks. **Passing all checks does not guarantee that a password is secure.**

### Planned

- **File encryption and decryption:** Protect files using password-based, authenticated encryption.
- **Secure vault:** Organize and manage protected files.
- **Activity history:** Record relevant application operations.
- **Graphical interface:** Build a user-friendly interface for managing the application's features.

## Technologies

- **`Python`** — Core application language
- **`hashlib`** — SHA-256 hashing
- **`pathlib`** — File and directory path handling
- **`secrets`:** Used for cryptographically strong random password generation.
- **`string`:** Provides character sets for password generation and special-character validation.

## Project Structure

```text
BlackBox/
├── integrity/
│   ├── __init__.py
│   └── checksum.py
├── password_utils/
│   ├── __init__.py
│   ├── pass_gen.py
│   └── pass_checker.py
├── BlackBox.py
├── README.md
└── .gitignore
```

The `integrity` package contains file hashing and integrity-checking functionality. The `password_utils` package contains the password generation and password strength checker module. `BlackBox.py` is the current application entry point.

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

BlackBox uses SHA-256 to produce a fixed-length hash from file contents. Even a small change to a file will ordinarily produce a different hash.

For folders, the integrity module processes files in a consistent sorted order and incorporates their relative paths and content hashes into a combined hash.

Comparing a newly calculated hash with a previously recorded hash helps detect changes to file contents, file names, or the folder's file structure.

## How Password Generation Works

BlackBox uses Python's `secrets` module to generate random passwords. Users can configure the minimum number of uppercase letters, lowercase letters, digits, and symbols required in the generated password.

The generator is designed to produce unpredictable passwords using cryptographically strong randomness.

## How Password Strength Checking Works

BlackBox evaluates passwords against five requirements: a minimum length of 12 characters, at least 2 uppercase letters, 2 lowercase letters, 2 digits, and 2 special characters.

The checker reports which requirements are not met and how many of the five tests failed.

**Limitations:** This is a basic rule-based checker. It does not detect common passwords, dictionary words, predictable patterns, or estimate resistance to password-guessing attacks. Passing all checks does not guarantee that a password is secure.

## Project Status

**In development.**

The project currently includes three independent modules:

- **File integrity checker:** Calculates and verifies SHA-256 hashes for files and folders, including nested folders.
- **Password generator:** Generates random passwords using Python's `secrets` module and configurable character requirements.
- **Password strength checker:** Validates passwords against minimum length and character composition requirements.

The modules are developed and tested independently.Integration into the main application is still in progress, with planned extensions including file encryption and decryption, secure vault management, activity history, and a graphical interface.

This project is intended for learning and demonstration. It has not yet been validated as a production-grade security application.

## Goals

- Apply Python programming concepts to a practical project.
- Develop a modular and maintainable codebase.
- Explore file integrity and other security-related concepts.
- Expand the application through independently developed features.