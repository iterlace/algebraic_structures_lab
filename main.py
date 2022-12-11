import time

from methods import *


def run_pollard():
    n = int(input("n: "))
    result = factorize_by_pollard(n)
    print(f"factors = {result}")


def run_bsgs():
    """
    Sample input:
     - bsgs(9, 150, 997) = None
     - bsgs(5, 8, 43) = 15
     - bsgs(7, 15, 131) = 8
    """
    print('enter variables for a "g^x = h (mod p)"')
    g = int(input("g: "))
    h = int(input("h: "))
    p = int(input("p: "))

    result = bsgs(g, h, p)
    print(f"result = {result}")


def run_phi():
    """
    Sample input:
     - phi(306) = 96
     - phi(230) = 88
     - phi(161) = 132
     - phi(89) = 88
     - phi(497) = 420
     - phi(500) = 200
    """
    n = int(input("n: "))
    result = phi(n)
    print(f"phi({n}) = {result}")


def run_mu():
    """
    Sample input:
     - mu(10) = 1
     - mu(11) = -1
     - mu(20) = 0
    """

    n = int(input("n: "))
    result = mu(n)
    print(f"mu({n}) = {result}")


def run_jacobi():
    """
    Sample input:
     - jacobi(10, 21) = -1
     - jacobi(1, 3) = 1
     - jacobi(6, 9) = 0
    """

    a = int(input("a: "))
    p = int(input("p: "))
    result = jacobi_symbol(a, p)
    print(f"jacobi({a}, {p}) = {result}")


def run_legendre():
    """
    Sample input:
     - legendre(3, 5) = -1
     - legendre(0, 5) = 0
     - legendre(4, 11) = 0
    """

    a = int(input("a: "))
    p = int(input("p: "))
    result = legendre_symbol(a, p)
    print(f"legendre({a}, {p}) = {result}")


def run_solovay_strassen():
    """
    Sample input:
     - is_prime(19) = True
     - is_prime(10) = False
     - is_prime(10, 1) = 0
    """

    n = int(input("n: "))
    result = is_prime_solovay_strassen(n=n)
    print(f"is_prime({n}) = {result}")


def main():
    methods_map = {
        1: run_pollard,
        2: run_bsgs,
        3: run_phi,
        4: run_mu,
        5: run_jacobi,
        6: run_legendre,
        7: run_solovay_strassen,
    }
    while True:
        print(
            "Available methods:\n"
            "1. Factorization by Pollard\n"
            "2. Baby-step Giant-step\n"
            "3. Phi (Euler's function)\n"
            "4. Mu (Mobius Function)\n"
            "5. Jacobi symbol\n"
            "6. Legendre symbol\n"
            "7. Solovay Strassen primality test\n"
            "exit. Quit the program"
        )
        selection = input("Select a method to run (1-7): ").strip().lower()

        if selection == "exit":
            break

        if not selection.isnumeric() or int(selection) not in methods_map.keys():
            print("Selected method doesn't exist.")
            continue

        _callable = methods_map[int(selection)]
        try:
            _callable()
        except Exception as e:
            print(
                f"Encountered an unexpected error. "
                f"Please, try again with another input.\n"
                f"Error: {e}"
            )
        time.sleep(3)
        print()


if __name__ == "__main__":
    main()
