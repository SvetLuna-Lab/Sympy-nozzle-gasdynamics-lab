# SymPy Nozzle Gasdynamics Lab

This repository is a small laboratory for **quasi-1D nozzle gasdynamics**
built on top of SymPy. Here the nozzle is treated not only as a component of a
rocket engine, but also as an **organ** through which the flow passes, and as a
**collider-like channel** where energy and momentum are redistributed along the
path.

The goal of the project is to make nozzle gasdynamics formulas:

- transparent (symbolic derivations instead of a black box),
- convenient (numeric functions for profiles),
- visual (simple engineering plots).

---

## Idea: nozzle as organ and as collider

In the classical quasi-1D model, a nozzle is described by:

- uniform flow across each cross-section;
- pressure, temperature and velocity changing only along the axis;
- a critical region (throat) where the flow becomes sonic (Mach 1).

If we look at the nozzle as an **organ**, then:

- the inlet is like the “atrium” of the system: the flow is still slow,
  parameters are close to stagnation values (T₀, p₀);
- the throat is where the system compresses the flow to its limit:
  speed reaches Mach 1, area is minimal, acceleration is maximal;
- the exit is the “exhalation” zone: the flow is already supersonic,
  pressure drops, energy unfolds into a jet.

If we look at the nozzle as a **collider-like channel**, then:

- the converging section is an accelerating path where stagnation
  potential (p₀, T₀) is converted into kinetic energy;
- the throat is the “narrow gate” where the flow crosses the sonic barrier;
- the diverging section is where the jet carries most of the thrust.

In both views, the same mathematics sits underneath:
isentropic relations and the area–Mach relation.

---

## What this laboratory does

The project is organized in three layers:

1. **Symbolic core (`src/symgas/symbolic_nozzle.py`)**

   - the specific heat ratio γ is defined (e.g. 1.4 for air);
   - symbolic formulas are derived for:

     - \(T/T_0(M)\) — static-to-stagnation temperature ratio;
     - \(p/p_0(M)\) — static-to-stagnation pressure ratio;
     - \(\rho/\rho_0(M)\) — density ratio;
     - \(A/A^*(M)\) — area–Mach relation.

   All of these are plain SymPy expressions that can be inspected,
   simplified, differentiated.

2. **Numeric wrapper (`src/symgas/numerics.py`)**

   - the `IsentropicNozzleNumeric` class converts symbolic expressions
     into NumPy-based functions;
   - for a given Mach profile \(M(x)\) you can compute:

     - \(T(x)\), \(p(x)\), \(\rho(x)\),
     - \(A(x)/A^*\) along the nozzle;

   - you only need to specify stagnation parameters `T0`, `p0`
     (and optionally `rho0`).

3. **Plots and notebooks**

   - `src/symgas/plots.py` provides simple engineering plots
     (Mach profile, pressure and temperature);
   - notebooks:

     - `01_symbolic_derivations.ipynb` — step-by-step symbolic derivations;
     - `02_nozzle_profiles.ipynb` — example profile from subsonic inlet
       through the throat to supersonic exit.

---

## Intended use

The lab does **not** aim to be a full nozzle design tool. It is:

- a learning instrument,
- a playground for SymPy-based derivations,
- a bridge between textbook equations and working scripts.

It is convenient for:

- tracing how formulas from a gasdynamics textbook translate into
  actual plots;
- seeing how symbolic expressions (SymPy) become numerical functions;
- using the nozzle as a compact, intuitive example of a **flow organ**
  and a **linear collider-like channel** for further studies.

---

## Connection to a broader picture

In a broader view:

- a nozzle can be seen as **one element in a larger cascade**:
  from combustion chamber → throat → jet → external flow;
- symbolic models (SymPy) form a basis for **intelligent interfaces**,
  where AI does not only “plug numbers into formulas” but also relies
  on the structure of equations;
- the analogy “collider as tubular bone” and “nozzle as organ”
  helps transfer intuition between biomechanics, physics and engineering.

This repository fixes one concrete fragment of that picture:
**quasi-1D nozzle gasdynamics**, implemented cleanly in both symbolic
and numeric form.
