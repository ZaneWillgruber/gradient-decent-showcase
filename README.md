# gradient-decent-showcase

A showcase of gradient descent, built for CSE 620.

## Requirements

- **Python 3.14** — pinned in [`.python-version`](.python-version) and required
  by `pyproject.toml` (`requires-python = ">=3.14"`).
- **[uv](https://docs.astral.sh/uv/)** — used for dependency resolution,
  virtual environments, and the build backend (`uv_build`)

### Installing uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# or, if you already have a package manager you prefer
brew install uv          # Homebrew
pipx install uv          # pipx
```

Restart your shell afterward, then confirm:

```bash
uv --version
```

## Setup

```bash
# 1. Clone
git clone https://github.com/ZaneWillgruber/gradient-decent-showcase.git
cd gradient-decent-showcase

# 2. Create the virtual environment and install the project (plus deps)
uv sync
```

## Everyday usage

Prefix commands with `uv run` and uv will use the project environment
automatically — no manual activation needed:

```bash
uv run gradient-decent-showcase        # run the console entry point
uv run python                          # REPL with the package importable
uv run python -c "import gradient_decent_showcase"
```

### Adding a dependency

```bash
uv add numpy                   # runtime dependency
uv add --dev pytest            # development-only dependency
```

## Project layout

```
gradient-decent-showcase/
├── pyproject.toml                        # project metadata, deps, entry point
├── .python-version                       # pins Python 3.14
└── src/
    └── gradient_decent_showcase/
        └── __init__.py                   # main() — the console entry point
```

## Troubleshooting

**`uv: command not found`** — the installer put uv in `~/.local/bin`, which may
not be on your `PATH`. Restart your shell, or add it:
`export PATH="$HOME/.local/bin:$PATH"`.

**"No interpreter found for Python 3.14"** — let uv fetch it:
`uv python install 3.14`, then re-run `uv sync`.

**`ModuleNotFoundError: gradient_decent_showcase`** — you're running a Python
outside the project environment. Use `uv run python ...`, or activate `.venv`
first.

**Environment feels stale or broken** — it's disposable; rebuild it:
`rm -rf .venv && uv sync`.
