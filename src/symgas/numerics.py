# src/symgas/numerics.py
"""
Numeric helpers for the symbolic nozzle gasdynamics core.

This module turns the symbolic isentropic relations into fast NumPy
functions and provides a small helper class for building 1D nozzle
profiles based on Mach number distributions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any

import numpy as np
import sympy as sp
from sympy.utilities.lambdify import lambdify

from .symbolic_nozzle import (
    mach,
    expressions_for_gamma,
)


@dataclass
class IsentropicNozzleNumeric:
    """
    Numeric wrapper around the symbolic isentropic relations.

    Parameters
    ----------
    gamma_value : float
        Specific heat ratio (e.g. 1.4 for air).
    """

    gamma_value: float = 1.4

    def __post_init__(self) -> None:
        exprs: Dict[str, sp.Expr] = expressions_for_gamma(self.gamma_value)

        # Lambdified functions: each takes Mach number M (scalar or array-like)
        self._T_T0 = lambdify(mach, exprs["T_T0"], modules="numpy")
        self._p_p0 = lambdify(mach, exprs["p_p0"], modules="numpy")
        self._rho_rho0 = lambdify(mach, exprs["rho_rho0"], modules="numpy")
        self._A_Astar = lambdify(mach, exprs["A_Astar"], modules="numpy")

    # ------------------------------------------------------------------
    # Basic non-dimensional ratios
    # ------------------------------------------------------------------

    def T_T0(self, M: Any) -> np.ndarray:
        """Return T/T0 as a function of Mach number M."""
        return np.asarray(self._T_T0(M), dtype=float)

    def p_p0(self, M: Any) -> np.ndarray:
        """Return p/p0 as a function of Mach number M."""
        return np.asarray(self._p_p0(M), dtype=float)

    def rho_rho0(self, M: Any) -> np.ndarray:
        """Return rho/rho0 as a function of Mach number M."""
        return np.asarray(self._rho_rho0(M), dtype=float)

    def A_Astar(self, M: Any) -> np.ndarray:
        """Return A/A* as a function of Mach number M."""
        return np.asarray(self._A_Astar(M), dtype=float)

    # ------------------------------------------------------------------
    # Dimensional helpers
    # ------------------------------------------------------------------

    def dimensional_profiles(
        self,
        M: Any,
        T0: float = 300.0,
        p0: float = 1.0e5,
        rho0: float | None = None,
    ) -> Dict[str, np.ndarray]:
        """
        Given Mach number distribution M, return dimensional profiles.

        Parameters
        ----------
        M : array-like
            Mach number(s).
        T0 : float
            Stagnation temperature [K].
        p0 : float
            Stagnation pressure [Pa].
        rho0 : float, optional
            Stagnation density [kg/m^3]. If None, it will be derived from
            p0, T0 and R = 287 J/(kg*K) assuming ideal gas.

        Returns
        -------
        dict
            {
              "M": M_array,
              "T": T_array,
              "p": p_array,
              "rho": rho_array,
              "A_Astar": A_Astar_array,
            }
        """
        M_arr = np.asarray(M, dtype=float)

        if rho0 is None:
            # Very simple ideal gas assumption for air
            R = 287.0
            rho0 = p0 / (R * T0)

        T_T0 = self.T_T0(M_arr)
        p_p0 = self.p_p0(M_arr)
        rho_rho0 = self.rho_rho0(M_arr)
        A_Astar = self.A_Astar(M_arr)

        T = T_T0 * T0
        p = p_p0 * p0
        rho = rho_rho0 * rho0

        return {
            "M": M_arr,
            "T": T,
            "p": p,
            "rho": rho,
            "A_Astar": A_Astar,
        }
