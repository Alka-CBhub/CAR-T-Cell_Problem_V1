###############################################
#
#    Utilities for Finding Steady States
#
###############################################

# Import necessary libraries
import numpy as np
from scipy.optimize import fsolve


# ------------------------------------------------------------------
    # 1) Round very small steady states to zero. 
# ------------------------------------------------------------------

def round_very_small(x_ss, tol=1e-10):
    """
    Set |x_ss|<tol to exactly 0.
    
    Parameters
    ----------
    x_ss : float or np.ndarray
        Input value or array of values to round.
    tol : float, optional
        Threshold below which numbers are considered zero.

    Returns
    -------
    float or np.ndarray
        The "rounded" result: anything with |value| < tol is replaced by 0.
    """
    
    if np.isscalar(x_ss):    #  A single scalar
        return 0 if abs(x_ss)<tol else x_ss
    else:                    # An array of steady states
        return np.where(np.abs(x_ss)<tol, 0.0, x_ss)

# ------------------------------------------------------------------
    # 2) Define bounds for the variables
# ------------------------------------------------------------------
def bound_range(value, bound):
    """
    True if `value` lies inside `bound`.

    Parameters
    ----------
    value : float
        The coordinate being tested.
    bound : None or a tuple
        * None -> unbounded
        * (low, high) -> two-sided  (low <= x <= high)
        * (None, high)-> upper-bounded (x <= high)
        * (low, None) -> lower-bounded (x >= low)
    """
    if bound is None:
        return True
    low, high = bound
    if low is None:
        return value <= high
    if high is None:
        return value >= low
    return low <= value <= high


# ------------------------------------------------------------------
    # 3) Find steady states
# ------------------------------------------------------------------
def find_steady_states(
    system_func,
    num_vars,
    num_samples=500,
    tol=1e-8,
    domain=None,
    zero_tol=1e-10,
    verbose=False,
    seed=None,
):
    """
    Identify unique steady states of an n-dimensional dynamical system
    by solving dot(X) = 0 from multiple random initial guesses.

    Parameters
    ----------
    system_func : callable
        Accepts an (n,) vector, returns the time-derivatives (n,)
        That is, [dx1/dt, ..., dxn/dt] for input state [x1, ..., xn].

    num_vars : int
        Dimension of the state vector.

    num_samples : int, default 500
        Number of random initial guesses.

    tol : float, default 1e-8
        Absolute tolerance when deciding two roots are identical.

    domain : list[tuple or None], default [(0, 1)]*n
        Per-variable bounds:
            * (low, high)-> low <= x <= high
            * (low, None)-> x >= low
            * (None, high)-> x <= high
            * None -> unbounded (no check)

        **Note**  A finite interval is still required for *sampling*; if intervals 
        are specified as half-open or unbounded, the corresponding initial guesses are
        drawn from [0, 1] by default.  

    zero_tol : float, default 1e-10
        Values (|x| < zero_tol) are rounded to zero after convergence.

    verbose : bool, default False
        Print a short log of accepted/rejected guesses.

    seed : int or None
        Seed for reproducibility.

    Returns
    -------
    list[np.ndarray]
        Lexicographically sorted list of unique steady-state vectors.
    """

    # ------------------------------------------------------------------
    #  Handle the domain and create an array for sampling
    # ------------------------------------------------------------------
    if domain is None:
        domain = [(0.0, 1.0)] * num_vars
    if len(domain) != num_vars:
        raise ValueError("`domain` length must equal `num_vars`")

    lows, highs = [], []
    for bnd in domain:
        # Unbounded or half-open --> fall back on [0, 1] for **sampling only**
        if bnd is None or bnd[0] is None or bnd[1] is None:
            lows.append(0.0)
            highs.append(1.0)
        else:
            lows.append(bnd[0])
            highs.append(bnd[1])

    rng = np.random.default_rng(seed)
    guesses = rng.uniform(low=lows, high=highs, size=(num_samples, num_vars))

    # ------------------------------------------------------------------
    # Iterate over guesses, applying fsolve and the various filters
    # ------------------------------------------------------------------
    roots = []
    for i, guess in enumerate(guesses, start=1):
        sol, info, ier, _ = fsolve(system_func, guess, full_output=True)

        if ier != 1:  # fsolve did not converge
            if verbose:
                print(f"Guess {i:3d}: did not converge")
            continue

        sol = round_very_small(sol, tol=zero_tol)

        # Discard if outside the bounds
        if not all(bound_range(val, bnd) for val, bnd in zip(sol, domain)):
            if verbose:
                print(f"Guess {i:3d}: out of bounds {np.round(sol, 4)}")
            continue

        # Discard duplicates
        if any(np.allclose(sol, root, atol=tol) for root in roots):
            continue

        roots.append(sol)
        if verbose:
            print(f"Guess {i:3d}: accepted root {np.round(sol, 4)}")

    # Make sure consistent ordering
    roots.sort(key=lambda r: tuple(np.round(r, 12)))
    return roots
 