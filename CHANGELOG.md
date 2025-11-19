# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/)
and this project (for now) uses a simple semantic-style versioning.

---

## [0.1.0] - 2025-11-19

### Added

- Initial project structure for **sympy-nozzle-gasdynamics-lab**:
  - `src/symgas/__init__.py` as a lightweight package entry point.
  - `src/symgas/symbolic_nozzle.py` with symbolic isentropic relations:
    - temperature ratio `T/T0(M)`,
    - pressure ratio `p/p0(M)`,
    - density ratio `rho/rho0(M)`,
    - area–Mach relation `A/A*(M)`.

- Numeric helper:
  - `src/symgas/numerics.py` with `IsentropicNozzleNumeric`:
    - lambdified SymPy expressions to NumPy functions,
    - `dimensional_profiles(...)` for `M(x) → T(x), p(x), rho(x), A/A*`.

- Plotting utilities:
  - `src/symgas/plots.py`:
    - `plot_mach_profile(...)`,
    - `plot_pressure_temperature_profiles(...)`.

- Notebooks:
  - `notebooks/01_symbolic_derivations.ipynb` —
    basic symbolic walkthrough for `gamma = 1.4`.
  - `notebooks/02_nozzle_profiles.ipynb` —
    sample Mach profile with dimensional `T(x), p(x)` plots.

- Tests:
  - `tests/test_symbolic_nozzle.py` —
    basic checks for symbolic relations and `expressions_for_gamma(...)`.

- Tooling:
  - `requirements.txt` with core dependencies (SymPy, NumPy, Matplotlib).
  - `requirements-dev.txt` with pytest.
  - `pytest.ini` to configure test discovery.
