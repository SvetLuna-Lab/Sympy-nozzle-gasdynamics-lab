# SymPy Nozzle Gasdynamics Lab — Overview

This project is a small **symbolic laboratory** for quasi-1D gasdynamics
in convergent or convergent–divergent nozzles.

The main goals are:

1. To derive the standard isentropic relations for a perfect gas
   **symbolically** using SymPy, in a transparent way.
2. To turn these symbolic expressions into **numerical tools**
   (NumPy functions) suitable for quick parametric studies.
3. To provide **notebooks** that read like a hybrid of a textbook,
   a lab notebook and a code walkthrough.

The project is intentionally minimalistic: it focuses on a few core relations
(p/p0, T/T0, rho/rho0, A/A*) and clean code, rather than trying to cover all
aspects of compressible flow.

Future extensions may include:

- handling subsonic and supersonic branches of the area–Mach relation;
- sample nozzle geometries with x → A(x) profiles;
- basic loss models (non-ideal expansion, friction).

The code is structured as a small Python package (`symgas`) and can be used
both from notebooks and from standalone scripts.
