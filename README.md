Here’s a more concise and minimal version of the `README.md`:

---

# Codebase to Text

`Codebase-to-Text` is a Python utility that clones a Git repository and extracts the contents of all files into a single text file. This is useful for feeding into an LLM or similar use cases.

## Features

- Clone any public Git repository.
- Optionally filter files by extensions.
- Optionally process files in a specific subdirectory.
- Outputs all content into a single annotated text file.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/codebase-to-text.git
   cd codebase-to-text
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python3 codebase-to-text.py <repo_url>
```

Example:

```bash
python3 codebase-to-text.py https://github.com/opencontainers/runc.git
```

### Optional Flags

- **Filter by extensions**: Use `--extensions` or `-e` to include specific file types. Example:

  ```bash
  python3 codebase-to-text.py https://github.com/opencontainers/runc.git --extensions .py,.md
  ```

- **Specify a subdirectory**: Use `--subdir` or `-s` to process only a specific subdirectory. Example:

  ```bash
  python3 codebase-to-text.py https://github.com/opencontainers/runc.git --subdir src
  ```

### Output

The tool creates an output file in the `out/` directory named `<repo-owner-repo-name>-<timestamp>.txt`, containing the concatenated file contents.

---

This is a simplified overview focusing on key information to get users started quickly.