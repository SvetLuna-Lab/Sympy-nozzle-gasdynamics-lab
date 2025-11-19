# src/symgas/plots.py
"""
Plotting utilities for nozzle gasdynamics profiles.

These helpers are intentionally minimal and focus on:
- Mach number vs. station index or x;
- pressure / temperature vs. station index or x.
"""

from __future__ import annotations

from typing import Sequence, Optional

import numpy as np
import matplotlib.pyplot as plt


def plot_mach_profile(
    x: Sequence[float],
    M: Sequence[float],
    title: str = "Mach number profile",
    xlabel: str = "Station",
) -> None:
    """
    Plot Mach number profile along a nozzle (or a generic 1D line).

    Parameters
    ----------
    x : sequence of float
        Station coordinate (could be index or physical x).
    M : sequence of float
        Mach number at each station.
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    """
    x_arr = np.asarray(x, dtype=float)
    M_arr = np.asarray(M, dtype=float)

    fig, ax = plt.subplots()
    ax.plot(x_arr, M_arr, marker="o")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Mach number M")
    ax.set_title(title)
    ax.grid(True)
    plt.tight_layout()


def plot_pressure_temperature_profiles(
    x: Sequence[float],
    p: Sequence[float],
    T: Sequence[float],
    title: str = "Pressure and temperature profiles",
    xlabel: str = "Station",
    p_label: str = "Pressure [Pa]",
    T_label: str = "Temperature [K]",
) -> None:
    """
    Plot pressure and temperature profiles along a nozzle.

    Parameters
    ----------
    x : sequence of float
        Station coordinate.
    p : sequence of float
        Static pressure at each station [Pa].
    T : sequence of float
        Static temperature at each station [K].
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    p_label : str
        Label for the pressure axis.
    T_label : str
        Label for the temperature axis.
    """
    x_arr = np.asarray(x, dtype=float)
    p_arr = np.asarray(p, dtype=float)
    T_arr = np.asarray(T, dtype=float)

    fig, ax1 = plt.subplots()

    ax1.plot(x_arr, p_arr, marker="o")
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(p_label)
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(x_arr, T_arr, marker="s", linestyle="--")
    ax2.set_ylabel(T_label)

    fig.suptitle(title)
    fig.tight_layout()
