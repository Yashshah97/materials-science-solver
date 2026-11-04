"""Demo for Materials Science Constraint Solver."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import materials_science_solver

print("Materials Science Constraint Solver", "v" + materials_science_solver.__version__)
print("modules:", [m for m in dir(materials_science_solver) if not m.startswith('_')])
