import math
import random
from math import gcd
from typing import List, Tuple

# The max value that 4-byte signed integer can contain
INT_MAX = 2147483647


def factorize_by_pollard(n: int) -> Tuple[int, int]:
    values = (0, 0)
    x = random.randint(0, min(n, INT_MAX))
    y = x
    _gcd = 1

    while _gcd == 1:
        x = _f(x, n)
        y = _f(_f(y, n), n)
        _gcd = math.gcd(n, abs(x - y))

    if _gcd != n:
        values = (_gcd, n // _gcd)

    return values


def _f(x: int, n: int) -> int:
    return (x**2 + 1) % n
