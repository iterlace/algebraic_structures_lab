import random

from ._4_legendre_jacobi import legendre_symbol


def is_prime_solovay_strassen(n: int, k: int = 10) -> bool:
    assert n > 0, "requirements: n > 0"

    if n in (1, 2):
        return True

    if not n & 1:
        # All even numbers are not prime by default
        return False

    for i in range(k):
        a = random.randint(2, n - 1)
        x = legendre_symbol(a, n)
        y = pow(a, (n - 1) // 2, n)
        if (x == 0) or (y != x % n):
            return False

    return True
