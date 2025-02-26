# python_docs_hook Package

Internal package documentation for the Python documentation generator pre-commit hook.

## Package Structure

- `__init__.py` - Package initialization and version information
- `main.py` - Core implementation of the documentation generator

## API Documentation

<!-- BEGIN_PY_DOCS -->
## main.py

### Functions

#### `extract_docstrings(filename)`

Extract docstrings from Python file.

Args:
    filename: Path to the Python file to process

Returns:
    Dictionary containing module and function documentation

#### `generate_markdown(filename, docs)`

Generate markdown documentation from docstrings.

Args:
    filename: Name of the source file
    docs: Dictionary containing extracted documentation

Returns:
    Formatted markdown string

#### `is_path_allowed(source_dir, allowed_paths)`

Check if the source directory is in allowed paths.

Args:
    source_dir: Directory to check
    allowed_paths: List of allowed paths

Returns:
    True if directory is allowed, False otherwise

#### `update_readme(content, source_file, allowed_paths)`

Update README.md in the same directory as the source file.

Args:
    content: Generated markdown content
    source_file: Path to the source Python file
    allowed_paths: List of paths where README.md files should be generated

#### `main()`

Main function to process Python files and generate documentation.

Returns:
    Exit code (0 for success, 1 for failure)

<!-- END_PY_DOCS -->

## Development

This package contains the core functionality of the pre-commit hook. The main components are:

1. AST-based docstring extraction
2. Markdown generation
3. README file management

For usage instructions, see the project's main README.md in the root directory.
