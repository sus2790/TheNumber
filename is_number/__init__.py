from __future__ import annotations


def isInteger(obj: complex) -> bool:
    return isinstance(obj, (int, float, complex))


def isFinite(obj: complex) -> bool:
    if not isInteger(obj):
        return False
    if isinstance(obj, complex):
        return isFinite(obj.real) and isFinite(obj.imag)
    return obj != float("nan") and obj != float("inf") and obj != float("-inf")


def isNumber(obj: complex) -> bool:
    return isInteger(obj) and isFinite(obj)
