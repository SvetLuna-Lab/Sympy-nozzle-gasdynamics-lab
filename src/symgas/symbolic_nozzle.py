# src/symgas/symbolic_nozzle.py
"""
Symbolic core for quasi-1D isentropic nozzle flow.

This module defines:

- gamma: specific heat ratio (symbolic);
- M: Mach number;
- isentropic relations for p/p0, T/T0, rho/rho0;
- area-Mach relation A/A* as a symbolic expression.

We deliberately keep the core formulas small and readable
to make this module a teaching tool, not a black-box library.
"""

import sympy as sp

# ----------------------------------------------------------------------
# Symbols
# ----------------------------------------------------------------------

# Specific heat ratio (k = gamma)
gamma = sp.symbols("gamma", positive=True)
# Mach number
mach = sp.symbols("M", positive=True)

# ----------------------------------------------------------------------
# Isentropic relations for a perfect gas
# ----------------------------------------------------------------------
# Reference: standard compressible flow relations for a calorically perfect gas.


def temperature_ratio_isentropic(g: sp.Symbol | float = gamma) -> sp.Expr:
    """
    Return symbolic expression for T / T0 as a function of Mach number M.

    T / T0 = 1 / (1 + (gamma - 1)/2 * M^2)
    """
    M = mach
    return 1 / (1 + (g - 1) / 2 * M**2)


def pressure_ratio_isentropic(g: sp.Symbol | float = gamma) -> sp.Expr:
    """
    Return symbolic expression for p / p0 as a function of Mach number M.

    p / p0 = (T / T0)^(gamma / (gamma - 1))
    """
    T_T0 = temperature_ratio_isentropic(g)
    return T_T0 ** (g / (g - 1))


def density_ratio_isentropic(g: sp.Symbol | float = gamma) -> sp.Expr:
    """
    Return symbolic expression for rho / rho0 as a function of Mach number M.

    rho / rho0 = (T / T0)^(1 / (gamma - 1))
    """
    T_T0 = temperature_ratio_isentropic(g)
    return T_T0 ** (1 / (g - 1))


# ----------------------------------------------------------------------
# Area–Mach relation (A / A*)
# ----------------------------------------------------------------------
# For a quasi-1D isentropic flow:
#
#   A / A* = 1/M * [ (2/(gamma+1)) * (1 + (gamma-1)/2 * M^2) ]^((gamma+1)/(2*(gamma-1)))
#
# where A* is the area at the sonic throat (M = 1).


def area_mach_relation(g: sp.Symbol | float = gamma) -> sp.Expr:
    """
    Return symbolic expression for the area-Mach relation A/A* as a function of M.

    A / A* = 1/M * [ (2/(gamma+1)) * (1 + (gamma-1)/2 * M^2) ]^((gamma+1)/(2*(gamma-1)))

    Note:
    - For A/A* > 1, there are two possible Mach numbers (subsonic and supersonic branch).
    - This function returns the symbolic expression; numerical inversion is handled elsewhere.
    """
    M = mach
    term = (2 / (g + 1)) * (1 + (g - 1) / 2 * M**2)
    exponent = (g + 1) / (2 * (g - 1))
    return (1 / M) * term**exponent


# ----------------------------------------------------------------------
# Convenience: simplified expressions for a given gamma (e.g. air: 1.4)
# ----------------------------------------------------------------------


def expressions_for_gamma(g_value: float = 1.4) -> dict[str, sp.Expr]:
    """
    Return a dictionary with simplified expressions for a specific gamma value.

    Parameters
    ----------
    g_value : float
        Specific heat ratio (e.g. 1.4 for air).

    Returns
    -------
    dict
        {
          "T_T0":  T/T0(M),
          "p_p0":  p/p0(M),
          "rho_rho0": rho/rho0(M),
          "A_Astar": A/A*(M)
        }
    """
    g_sub = {gamma: g_value}

    T_T0 = sp.simplify(temperature_ratio_isentropic(gamma).subs(g_sub))
    p_p0 = sp.simplify(pressure_ratio_isentropic(gamma).subs(g_sub))
    rho_rho0 = sp.simplify(density_ratio_isentropic(gamma).subs(g_sub))
    A_Astar = sp.simplify(area_mach_relation(gamma).subs(g_sub))

    return {
        "T_T0": T_T0,
        "p_p0": p_p0,
        "rho_rho0": rho_rho0,
        "A_Astar": A_Astar,
    }
