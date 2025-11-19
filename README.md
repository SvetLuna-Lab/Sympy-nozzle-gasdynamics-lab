# SymPy Nozzle Gasdynamics Lab

Small laboratory project for **quasi-1D nozzle gasdynamics** with a focus on
**symbolic derivations** using SymPy and clean engineering intuition.

Core idea:

- start from the standard 1D isentropic relations for a perfect gas;
- derive key formulas symbolically (Mach number, pressure and temperature ratios,
  area–Mach relation, etc.);
- turn symbolic expressions into fast numerical functions;
- visualize velocity, pressure and temperature profiles along a nozzle.

The project is designed as a learning and exploration tool:
somewhere between a textbook, a code library, and an engineering notebook.

---

## Features

- **Symbolic core (SymPy)**  
  - isentropic flow relations for perfect gas;  
  - Mach–area relation \(A/A^\*\)(M) for subsonic and supersonic branches;  
  - pressure and temperature ratios \(p/p_0, T/T_0\) as symbolic expressions.

- **Numeric wrapper (NumPy)**  
  - lambdified functions for fast evaluation;  
  - helpers to build 1D profiles along the nozzle (x, A(x), M(x), p(x), T(x)).

- **Engineering plots (Matplotlib)**  
  - basic nozzle profiles (Mach, pressure, temperature, density);  
  - ready to plug into Jupyter notebooks.

- **Notebooks for learning**  
  - `01_symbolic_derivations.ipynb` — step-by-step derivations;  
  - `02_nozzle_profiles.ipynb` — example nozzles and flow regimes.

---

## Repository structure

```text
src/symgas/
  __init__.py          # package marker
  symbolic_nozzle.py   # SymPy formulas (symbolic core)
  numerics.py          # lambdified NumPy functions
  plots.py             # plotting utilities

notebooks/
  01_symbolic_derivations.ipynb  # symbolic walkthrough
  02_nozzle_profiles.ipynb       # sample nozzle profiles

docs/
  Overview_EN.md       # conceptual overview and usage examples

tests/
  test_symbolic_nozzle.py  # basic checks for symbolic relations



Quickstart

Install dependencies:

pip install -r requirements.txt


Example usage (Python):

from symgas.symbolic_nozzle import (
    gamma,
    mach,
    pressure_ratio_isentropic,
    temperature_ratio_isentropic,
    area_mach_relation
)

# Set specific heat ratio for air
g = 1.4

# Example symbolic expressions
p_p0_expr = pressure_ratio_isentropic(g)
T_T0_expr = temperature_ratio_isentropic(g)
A_Astar_expr = area_mach_relation(g)

print("p/p0 =", p_p0_expr)
print("T/T0 =", T_T0_expr)
print("A/A* =", A_Astar_expr)


For interactive exploration, open the notebooks:

jupyter lab
# or
jupyter notebook


and run:

notebooks/01_symbolic_derivations.ipynb

notebooks/02_nozzle_profiles.ipynb


Status and roadmap

Current status (v0.1.0, prototype):

symbolic expressions for core isentropic relations;

basic structure for numeric wrappers and plots.

Planned:

helper functions for subsonic / supersonic branches of the area–Mach relation;

ready-made nozzle profiles (convergent–divergent, purely convergent);

more tests for limiting cases (M → 0, M → 1, M → 3+);

optional link to more advanced gasdynamic models.



