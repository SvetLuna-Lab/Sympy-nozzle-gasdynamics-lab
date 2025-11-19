# src/symgas/__init__.py
"""
symgas: SymPy-based quasi-1D gasdynamics lab for nozzle flows.

This package provides:

- symbolic derivations of basic isentropic relations for a perfect gas;
- expressions for pressure/temperature ratios and area–Mach relation;
- helpers to turn symbolic formulas into numerical functions and plots.
"""

from .symbolic_nozzle import (
    gamma,
    mach,
    pressure_ratio_isentropic,
    temperature_ratio_isentropic,
    density_ratio_isentropic,
    area_mach_relation,
)

__all__ = [
    "gamma",
    "mach",
    "pressure_ratio_isentropic",
    "temperature_ratio_isentropic",
    "density_ratio_isentropic",
    "area_mach_relation",
]
