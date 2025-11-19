# SymPy Nozzle Gasdynamics Lab

Small **SymPy-based laboratory** for quasi-1D nozzle gasdynamics.

The project focuses on:

- symbolic derivation of key **isentropic relations** for a perfect gas;
- turning these expressions into **NumPy-based numeric functions**;
- building and plotting simple **nozzle profiles** (Mach, pressure, temperature);
- serving as a **learning tool** between textbook formulas and working code.

This is not a full design code. It is a compact lab: part textbook,
part notebook, part Python package.

---

## Features

- **Symbolic core (SymPy)**  
  - temperature ratio \(T/T_0(M)\);  
  - pressure ratio \(p/p_0(M)\);  
  - density ratio \(\rho/\rho_0(M)\);  
  - area–Mach relation \(A/A^*(M)\).

- **Numeric wrapper (NumPy)**  
  - `IsentropicNozzleNumeric` for fast evaluation;  
  - `dimensional_profiles(...)` to get \(T(x), p(x), \rho(x), A/A^*(x)\) from a Mach profile.

- **Engineering plots (Matplotlib)**  
  - Mach number profile along a 1D line or nozzle;  
  - pressure + temperature profiles on the same x-axis.

- **Notebooks for exploration**  
  - step-by-step symbolic derivations;  
  - example nozzle profile from subsonic inlet through sonic throat to supersonic exit.

- **Tests**  
  - basic checks for symbolic expressions and numeric behavior (M → 0, M increasing).

For a more conceptual description (nozzle as **organ** and as **collider-like channel**),
see `docs/Overview_EN.md` and `docs/Overview_RU.md`.

---


## Project structure

```text
sympy-nozzle-gasdynamics-lab/
├─ src/
│  └─ symgas/
│     ├─ __init__.py              # package entry point, re-exports core helpers
│     ├─ symbolic_nozzle.py       # SymPy isentropic relations and A/A*(M)
│     ├─ numerics.py              # IsentropicNozzleNumeric: lambdified NumPy helpers
│     └─ plots.py                 # basic engineering plots (Mach, p, T)
├─ notebooks/
│  ├─ 01_symbolic_derivations.ipynb  # symbolic walkthrough for gamma = 1.4
│  └─ 02_nozzle_profiles.ipynb       # sample Mach profile and dimensional plots
├─ docs/
│  ├─ Overview_EN.md               # extended English overview (organ/collider view)
│  └─ Overview_RU.md               # Russian overview with the same idea
├─ tests/
│  ├─ test_symbolic_nozzle.py     # tests for symbolic relations and gamma-specific forms
│  └─ test_numerics.py            # tests for numeric wrapper behavior (M → 0, M sequence)
├─ CHANGELOG.md                   # project history (v0.1.0 and beyond)
├─ pyproject.toml                 # minimal packaging metadata (symgas package)
├─ requirements.txt               # runtime dependencies: SymPy, NumPy, Matplotlib
├─ requirements-dev.txt           # dev dependencies: pytest
├─ pytest.ini                     # pytest configuration
├─ .gitignore                     # ignore Python/Jupyter/build artifacts
└─ README.md                      # this file




## Installation

Create and activate a virtual environment (optional but recommended), then:

pip install -r requirements.txt


For editable install of the symgas package:

pip install -e .


After that you can import symgas from anywhere in that environment.



## Quick symbolic example

from symgas.symbolic_nozzle import (
    gamma,
    mach,
    temperature_ratio_isentropic,
    pressure_ratio_isentropic,
    density_ratio_isentropic,
    area_mach_relation,
    expressions_for_gamma,
)

# Set gamma = 1.4 (air)
g_val = 1.4

T_T0_expr = temperature_ratio_isentropic(gamma).subs({gamma: g_val})
p_p0_expr = pressure_ratio_isentropic(gamma).subs({gamma: g_val})
rho_rho0_expr = density_ratio_isentropic(gamma).subs({gamma: g_val})
A_Astar_expr = area_mach_relation(gamma).subs({gamma: g_val})

print("T/T0(M) =", T_T0_expr)
print("p/p0(M) =", p_p0_expr)
print("rho/rho0(M) =", rho_rho0_expr)
print("A/A*(M) =", A_Astar_expr)

# Or get all simplified expressions at once:
exprs = expressions_for_gamma(1.4)
print(exprs["T_T0"])
print(exprs["A_Astar"])


You can inspect and manipulate these SymPy expressions
(differentiate, simplify, substitute numeric values, etc.).


## Quick numeric example

import numpy as np

from symgas.numerics import IsentropicNozzleNumeric

# Create numeric helper for gamma = 1.4
nozzle = IsentropicNozzleNumeric(gamma_value=1.4)

# Simple Mach profile: from M=0.2 to M=2.0 along 21 stations
x = np.linspace(0.0, 1.0, 21)
M = np.linspace(0.2, 2.0, 21)

profiles = nozzle.dimensional_profiles(
    M=M,
    T0=300.0,      # stagnation temperature [K]
    p0=101325.0,   # stagnation pressure [Pa]
)

T = profiles["T"]
p = profiles["p"]
rho = profiles["rho"]
A_Astar = profiles["A_Astar"]

print("First few T values:", T[:5])
print("First few p values:", p[:5])
print("First few A/A* values:", A_Astar[:5])



## Plotting example (Jupyter)

Inside a notebook:


%matplotlib inline

from symgas.plots import (
    plot_mach_profile,
    plot_pressure_temperature_profiles,
)

plot_mach_profile(x, M, title="Mach number along the nozzle", xlabel="x (normalized)")
plot_pressure_temperature_profiles(
    x,
    p,
    T,
    title="Pressure and temperature along the nozzle",
    xlabel="x (normalized)",
    p_label="Pressure [Pa]",
    T_label="Temperature [K]",
)


For full examples, see:

notebooks/01_symbolic_derivations.ipynb

notebooks/02_nozzle_profiles.ipynb



## Running tests

Install dev requirements and run pytest:

pip install -r requirements-dev.txt
pytest


Tests include:

symbolic sanity checks (M → 0, A/A* at M = 1, consistency for fixed gamma);

numeric sanity checks (dimensional profiles at M = 0, monotonic pressure
decrease with increasing Mach in a simple sequence).



## Status and roadmap

Current status (v0.1.0):

symbolic core for isentropic relations and area–Mach relation;

numeric wrapper with dimensional profiles;

basic plots and example notebooks;

tests and minimal packaging via pyproject.toml.

Possible next steps:

helper functions for subsonic/supersonic branches of A/A*(M);

simple x → A(x) nozzle geometries and corresponding Mach distributions;

basic loss models (non-ideal expansion, friction) as extensions;

more detailed teaching notebooks for students.



## Versioning and changelog

This project follows a simple semantic-style versioning:

- **MAJOR** — breaking changes in the API or project structure,
- **MINOR** — new features that stay backward-compatible,
- **PATCH** — small fixes and internal improvements.

The current version is **`v0.1.0`**, which introduces the initial
symbolic core, numeric wrapper, plots, notebooks and packaging
for the `symgas` lab.

All notable changes are documented in `CHANGELOG.md`.  
For tagged versions and downloadable archives, see the GitHub
**Releases** section.



## License

This project is released under the MIT License.
See the LICENSE file for full text.
