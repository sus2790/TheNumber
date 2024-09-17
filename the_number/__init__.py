from __future__ import annotations


def isInteger(obj: complex) -> bool:
    """Check if the object is an integer, float, or complex number.

    Args:
    ----
        obj (complex | float | int): The object to check.

    Returns:
    -------
        bool: True if the object is an integer, float, or complex number, False otherwise.

    """
    return isinstance(obj, (int, float, complex))

def isInf(obj: complex) -> bool:
    """Check if the object is positive or negative infinity.

    Args:
    ----
        obj (complex | float | int): The object to check.

    Returns:
    -------
        bool: True if the object is positive or negative infinity, False otherwise.

    """
    return obj == float("inf") or obj == float("-inf")

def isNaN(obj: complex) -> bool:
    """Check if the object is NaN (Not a Number).

    Args:
    ----
        obj (complex | float | int): The object to check.

    Returns:
    -------
        bool: True if the object is NaN, False otherwise.

    """
    return isinstance(obj, float) and obj != obj

def isFinite(obj: complex) -> bool:
    """Check if the object is a finite number.

    Args:
    ----
        obj (complex | float | int): The object to check.

    Returns:
    -------
        bool: True if the object is a finite number, False otherwise.

    """
    if not isInteger(obj):
        return False
    if isinstance(obj, complex):
        return isFinite(obj.real) and isFinite(obj.imag)
    return not (isInf(obj) or isNaN(obj))

def isNumber(obj: complex) -> bool:
    """Check if the object is a valid number (integer, float, or complex) and not NaN.

    Args:
    ----
        obj (complex | float | int): The object to check.

    Returns:
    -------
        bool: True if the object is a valid number (including infinity) and not NaN, False otherwise.

    """
    return isInteger(obj) and not isNaN(obj)
