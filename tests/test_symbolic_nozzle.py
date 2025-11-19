# tests/test_symbolic_nozzle.py
"""
Basic tests for the symbolic nozzle gasdynamics core.

We check:
- limiting case M -> 0 (ratios tend to 1);
- sonic condition M = 1 gives A/A* ≈ 1;
- consistency between p/p0, T/T0 and rho/rho0 for a given gamma.
"""

import sympy as sp
import numpy as np

from symgas.symbolic_nozzle import (
    gamma,
    mach,
    temperature_ratio_isentropic,
    pressure_ratio_isentropic,
    density_ratio_isentropic,
    area_mach_relation,
    expressions_for_gamma,
)


def test_isentropic_ratios_at_M_zero():
    """At M = 0 all isentropic ratios should approach 1."""
    g_val = 1.4

    T_T0_expr = temperature_ratio_isentropic(gamma).subs({gamma: g_val})
    p_p0_expr = pressure_ratio_isentropic(gamma).subs({gamma: g_val})
    rho_rho0_expr = density_ratio_isentropic(gamma).subs({gamma: g_val})

    T_T0_at_0 = sp.N(T_T0_expr.subs({mach: 0.0}))
    p_p0_at_0 = sp.N(p_p0_expr.subs({mach: 0.0}))
    rho_rho0_at_0 = sp.N(rho_rho0_expr.subs({mach: 0.0}))

    assert sp.Abs(T_T0_at_0 - 1) < 1e-12
    assert sp.Abs(p_p0_at_0 - 1) < 1e-12
    assert sp.Abs(rho_rho0_at_0 - 1) < 1e-12


def test_area_mach_relation_at_M_one():
    """At M = 1 the area ratio A/A* should be 1 (sonic throat)."""
    g_val = 1.4
    A_Astar_expr = area_mach_relation(gamma).subs({gamma: g_val})

    A_Astar_at_1 = sp.N(A_Astar_expr.subs({mach: 1.0}))
    assert sp.Abs(A_Astar_at_1 - 1) < 1e-10


def test_expressions_for_gamma_consistency():
    """
    Check that expressions_for_gamma returns consistent expressions
    with the direct definitions for a given gamma.
    """
    g_val = 1.4
    exprs = expressions_for_gamma(g_val)

    T_T0_direct = temperature_ratio_isentropic(gamma).subs({gamma: g_val})
    p_p0_direct = pressure_ratio_isentropic(gamma).subs({gamma: g_val})
    rho_rho0_direct = density_ratio_isentropic(gamma).subs({gamma: g_val})
    A_Astar_direct = area_mach_relation(gamma).subs({gamma: g_val})

    M_val = 2.0  # some supersonic test value

    subs = {mach: M_val}

    for key, direct_expr in [
        ("T_T0", T_T0_direct),
        ("p_p0", p_p0_direct),
        ("rho_rho0", rho_rho0_direct),
        ("A_Astar", A_Astar_direct),
    ]:
        expr_pack = exprs[key]
        val_pack = float(sp.N(expr_pack.subs(subs)))
        val_direct = float(sp.N(direct_expr.subs(subs)))
        assert np.isclose(val_pack, val_direct, rtol=1e-12, atol=1e-12)
