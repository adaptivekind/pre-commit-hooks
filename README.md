# Extra pre-commit-hooks

A collection of additional pre-commit hooks for Git repositories. This package provides useful hooks to enhance your development workflow, including checking for untracked files that might need to be committed or ignored.

## Quick Start

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/adaptivekind/pre-commit-hooks
    rev: main
    hooks:
      - id: check-untracked-files
```

### Available Hooks

#### check-untracked-files

Checks for untracked files in your Git repository and warns about files that might need to be committed or added to `.gitignore`.

**Usage:**

```yaml
- id: check-untracked-files
  args: [--no-fail] # Optional: warn instead of failing
```

**Arguments:**

- `--no-fail`: Warn about untracked files but don't fail the hook

## Development

### Setup

Install development dependencies and pre-commit hooks:

```sh
pip install -e .
pre-commit install
```

### Testing Semantic Release

To test the semantic release process:

```sh
pip install python-semantic-release
semantic-release --help
semantic-release -v version
```
