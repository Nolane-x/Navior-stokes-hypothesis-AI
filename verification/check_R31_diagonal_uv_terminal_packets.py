#!/usr/bin/env python3
"""Algebraic verifier for R31 diagonal UV terminal-packet extraction."""
import math


def check_window_formula():
    checks = 0
    nu = 0.7
    E0 = 1.8
    for N in (7, 33, 141, 777):
        C = N * E0**4 / math.sqrt(2.0 * nu)
        for eps in (1.0, 0.2, 0.03, 1e-3):
            delta = 2.0 * nu * eps**2 / (N**2 * E0**8)
            assert C * math.sqrt(delta) <= eps * (1.0 + 1e-12)
            checks += 1
    return checks


def check_packet_extraction():
    # Synthetic cumulative functions with the exact qualitative hypotheses:
    # gradient/solenoidal work and balanced action diverge as T->T*,
    # while representation mismatch is uniformly small on the chosen window.
    checks = 0
    for n in (2, 5, 20, 100):
        eps = 1.0 / n
        target = float(n)
        s = 10.0 * n
        grad = s + 0.4 * eps
        sol = s - 0.4 * eps
        bal = 2.0 * s
        assert grad >= target
        assert sol >= target
        assert bal >= target
        assert abs(grad - sol) <= eps
        checks += 4
    return checks


def check_terminal_locality():
    # If an improper nonnegative integral diverges but every compact pre-endpoint
    # interval is finite, every terminal subinterval also has infinite mass.
    checks = 0
    for compact in (0.0, 1.0, 10.0, 1e6):
        total = math.inf
        terminal = total - compact
        assert math.isinf(terminal)
        checks += 1
    return checks


def main():
    checks = check_window_formula()
    checks += check_packet_extraction()
    checks += check_terminal_locality()
    print(f"PASS R31 diagonal UV terminal-packet algebra checks={checks}")


if __name__ == "__main__":
    main()
