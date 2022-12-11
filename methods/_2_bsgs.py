from math import ceil, sqrt


def bsgs(g, h, p):
    """
    Baby Step, Giant Step. The method to find a discrete logarithms.

    Returns x from "g^x = h (mod p)"
    p must be prime
    """
    M = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(M)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, M * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(M):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * M + tbl[y]

    # Solution not found
    return None
