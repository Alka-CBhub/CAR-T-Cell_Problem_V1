# ---------------------------------------------
# Utility functions to parse string‑based feature terms into SymPy expressions
# and assemble them (with coefficients) into symbolic right‑hand sides for ODEs.
# ---------------------------------------------


# Import necessary library
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)


# ---------------------------------------------
# Custom transformation rules for parsing math
# ---------------------------------------------
# These allow:
#   - "x^2" to be interpreted as "x**2"
#   - "xy" or "x y" to be interpreted as "x*y"
_transformations = (
    standard_transformations +
    (implicit_multiplication_application, convert_xor)
)

# -----------------------------------------------------
#  Convert a math-like string to SymPy expr
# -----------------------------------------------------
def parse_feature_expr(feat: str) -> sp.Expr:
    """
    Converts a math string like 'x^2 y' or '3xy' into a SymPy expression.
    
    Example:
        'x^2 y' --> x**2 * y

    Parameters:
        feat (str): A string representation of a feature term.

    Returns:
        sympy.Expr: A parsed SymPy expression.
    """
    return parse_expr(feat, transformations=_transformations)

# ------------------------------------------------------------------
# Convert a list of feature names into SymPy expressions
# ------------------------------------------------------------------
def build_expr_map(feature_names: list[str]) -> dict[str, sp.Expr]:
    """
    Creates a mapping from each feature string to its SymPy equivalent.
    
    Example:
        ['1', 'x', 'x^2'] --> {'1': 1, 'x': x, 'x^2': x**2}

    Parameters:
        feature_names (list of str): Feature strings from a model.

    Returns:
        dict: A dictionary mapping each feature name to a SymPy expression.
    """
    return {name: parse_feature_expr(name) for name in feature_names}

# ------------------------------------------------------
# Build a symbolic RHS using model coefficients
# ------------------------------------------------------
def build_symbolic_rhs(coeffs: list[float], feature_names: list[str]) -> sp.Expr:
    """
    Given a list of coefficients and feature names, return a full symbolic expression
    (e.g., right-hand side of a differential equation).
    
    Very small coefficients (e.g., < 1e-8) are ignored.

    Example:
        coeffs = [0.5, 0, -1.2]
        feature_names = ['x', 'y', 'x^2']
        --> 0.5*x - 1.2*x**2

    Parameters:
        coeffs (list of float): Coefficients for each feature.
        feature_names (list of str): Names like 'x', 'x^2', 'xy'.

    Returns:
        sympy.Expr: The full symbolic expression.
    """
    expr_map = build_expr_map(feature_names)
    return sum(
        c * expr_map[name]
        for c, name in zip(coeffs, feature_names)
        if abs(c) > 1e-8  # Change here 
    )
