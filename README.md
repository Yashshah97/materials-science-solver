# Materials Science Constraint Solver

This project is an open-source constraint solver designed to tackle complex problems in materials science, specifically focusing on the properties of crystalline lattices and alloys. With its flexible architecture and range of pluggable heuristics, users can adapt the solver to suit their specific needs, making it a valuable tool for researchers and engineers alike. By providing a comprehensive suite of benchmarks and documentation, this project aims to facilitate collaboration and advancement in the field of materials science constraint solving.

## What makes it unique

Combines crystal lattice and alloy properties with a heuristic solver with pluggable strategies and benchmarks — a niche where few ready-made tools exist.

## Features

- **`materials_science_solver/materials.py`** — Module containing data structures and constants for materials science
- **`materials_science_solver/solver.py`** — Heuristic constraint solver with pluggable strategies
- **`materials_science_solver/strategies.py`** — Module containing various solving strategies that can be plugged into the solver
- **`materials_science_solver/benchmarks.py`** — Module containing functions to run benchmarks on the solver's performance
- **`materials_science_solver/utils.py`** — Miscellaneous utility functions for the project, such as logging and parsing
- **`materials_science_solver/tests.py`** — Unit tests for the module using Python's built-in unittest framework

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/materials-science-solver.git
cd materials-science-solver

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
materials-science-solver/
├── materials_science_solver/
│   ├── materials.py
│   ├── solver.py
│   ├── strategies.py
│   ├── benchmarks.py
│   ├── utils.py
│   ├── tests.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **materials-science** · Archetype: **solver** ·
Built autonomously by JARVIS on 2026-11-03. MIT licensed.
