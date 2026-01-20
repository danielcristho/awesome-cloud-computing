# Contributing

Contributions are always welcome.

## Guidelines

- Add resources to the appropriate markdown files in `docs/en/` directory.
- Use the table format: `| [Name](https://example.com) | Short description. |`
- Keep descriptions concise and factual.
- Ensure links work and lead to legitimate resources.
- Use clean URLs without trailing slashes for homepages: `https://example.com` not `https://example.com/`
- Add new sections only when necessary.

## Pull Requests

- Keep PR focused: one primary logical change per PR.
- Use a clear title, for example: `Add Terraform to infrastructure tools`.
- Test your changes locally if possible using `just dev`.

## Content Organization

- **Main content** is in `docs/en/` directory
- **Website** is built from these markdown files
- **README.md** serves as a landing page directing to the website
- Changes to `docs/en/` automatically update the website

## Issues

- Use issues to report broken links, errors, or suggestions.
- Provide a short and clear description.

## Development Setup

Local setup is only required if you want to preview the site or work on larger changes.

### Prerequisites

- Install [`uv`](https://docs.astral.sh/uv) (Python package manager):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Install [`lychee`](https://github.com/lycheeverse/lychee) (Link checker)

```bash
cargo install lychee
```

> **Note**: You need to install `cargo` before: `curl https://sh.rustup.rs -sSf | sh`
> Or read the [guidelines](https://doc.rust-lang.org/cargo/getting-started/installation.html).

### Setup

**1. Fork and clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/awesome-cloud-computing.git && cd awesome-cloud-computing
```

**2. Setup Python environment (Python 3.13):**

Option A - Automatic (Recommended):

```bash
uv sync --extra dev
```

Option B - Manual virtual environment:

```bash
uv venv --python 3.13
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

**3. Start development server:**

```bash
uv run mkdocs serve
```

The site will be available at `http://127.0.0.1:8000`

### Optional: Install justfile for easier commands

If you want to use the task runner for convenience:

```bash
# On macOS: brew install just
# On Linux: cargo install just
# Or visit: https://github.com/casey/just#installation

# Then you can use:
just dev              # Start development server
just lint             # Run quality checks (fast, no link checking)
just check-links      # Check for broken links only
just check-all        # Run all checks including links (slower)
just create-lang <code_lang> # Create new language structure
just install-hooks    # Install pre-commit hooks
```

### Manual Commands

Without justfile, you can run commands directly:

```bash
# Start development server
uv run mkdocs serve
```

```bash
# Run all quality checks (includes markdown linting)
uv run pre-commit run --all-files
```

```bash
# Check for broken links only
lychee docs/en/**/*.md
```

```bash
# Create new language
uv run python scripts/create-language.py <code_lang>
```

### Pre-commit Hooks (Optional)

To automatically run quality checks before each commit:

```bash
# Install pre-commit hooks
uv run pre-commit install
```

```bash
# Run all checks (excludes link checking for performance)
uv run pre-commit run --all-files
```

The pre-commit hooks will automatically:

- Fix trailing whitespace and end-of-file issues
- Check markdown formatting with markdownlint
- Format Python code with ruff
- Format other files with prettier

**Note**: Link checking is handled separately via `just check-links` for better performance.

### Alternative Setup

If you don't want to use uv:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Start development server
mkdocs serve
```

## Adding Translations

To add a new language:

```bash
just create-lang es
just sync-langs

# Or manually

python scripts/create-language.py es
python scripts/sync-languages.py
```

## Quality Checks

```bash
just lint
just check-links

# Or manually

markdownlint README.md docs/**/*.md
lychee README.md docs/en/**/*.md
```
