# Codebase to Text

`Codebase-to-Text` is a Python utility that clones a Git repository and extracts the contents of all files within the repository into a single text file. This is helpful for plugging into a LLM.

## Features

- Clones any public Git repository to a temporary directory.
- Recursively traverses through all the files in the repository.
- Outputs the contents of each file into a single text file, with file paths annotated for clarity.
- Allows filtering files by extensions using a flag.
- Cleans up temporary files after execution.

## Prerequisites

- Python 3.x
- GitPython library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/codebase-to-text.git
   cd codebase-to-text
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   **Note:** You'll need to add `GitPython` to your `requirements.txt` if it's not already there:

   ```
   GitPython
   ```

## Usage

### Basic Usage

To use the tool, run the following command:

```bash
python3 codebase-to-text.py <repo_url>
```

Where `<repo_url>` is the URL of the Git repository you want to clone and process. For example:

```bash
python3 codebase-to-text.py https://github.com/opencontainers/runc.git
```

### Filtering by File Extensions

You can now filter which files to include in the output by specifying the file extensions using the `--extensions` or `-e` flag. This flag accepts a comma-separated list of file extensions.

For example, to include only `.py` and `.md` files:

```bash
python3 codebase-to-text.py https://github.com/opencontainers/runc.git --extensions .py,.md
```

### Output

- A text file will be generated in the `out/` directory. The file name will be in the format `<repo-owner-repo-name>-<timestamp>.txt`, where:
  - `<repo-owner-repo-name>` is the owner and name of the repository.
  - `<timestamp>` is the current timestamp when the script is executed (in `YYYYMMDDHHMMSS` format).

Example output file structure:

```
out/
└── opencontainers-runc-20240101000000.txt
```

### Temporary Directory

The tool clones the repository to a temporary directory `tmp/` during execution, which is automatically cleaned up after the process is complete.

### Logging

The script logs important events like cloning success, file read errors, file inclusion based on extensions, and paths of processed files.

## Example

Here's a complete example to extract the contents of a repository, filtering by specific file extensions:

```bash
python3 codebase-to-text.py https://github.com/opencontainers/runc.git --extensions .py,.sh
```

This will:
- Clone the `runc` repository into a temporary `tmp/` directory.
- Traverse through all `.py` and `.sh` files in the repository and write their contents into a file named `opencontainers-runc-<timestamp>.txt` inside the `out/` directory.
- Clean up the temporary directory after processing.

## Development

If you want to modify the script or contribute, feel free to fork the repository and submit pull requests.

### Running Locally

1. Fork the repository.
2. Clone your fork:

   ```bash
   git clone https://github.com/your-username/codebase-to-text.git
   ```

3. Make changes and test your updates.
