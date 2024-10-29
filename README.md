# Codebase to Text

`Codebase-to-Text` is a Python utility that clones a Git repository and extracts the contents of all files within the repository into a single text file. This tool helps in generating a consolidated view of the entire codebase for quick reference or analysis.

## Features

- Clones any public Git repository to a temporary directory.
- Recursively traverses through all the files in the repository.
- Outputs the contents of each file into a single text file, with file paths annotated for clarity.
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

### Output

- A text file will be generated in the `out/` directory. The file name will be in the format `<repo-name>-<timestamp>.txt`, where:
  - `<repo-name>` is the name of the repository.
  - `<timestamp>` is the current timestamp when the script is executed (in `YYYYMMDDHHMMSS` format).

Example output file structure:

```
out/
└── runc-20240101000000.txt
```

### Temporary Directory

The tool clones the repository to a temporary directory `tmp/` during execution, which is automatically cleaned up after the process is complete.

### Logging

The script logs important events like cloning success, file read errors, and the paths of processed files.

## Example

Here's a complete example to extract the contents of a repository:

```bash
python3 codebase-to-text.py https://github.com/opencontainers/runc.git
```

This will:
- Clone the `runc` repository into a temporary `tmp/` directory.
- Traverse through all files in the repository and write their contents into a file named `runc-<timestamp>.txt` inside the `out/` directory.
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

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.