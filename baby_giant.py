"""
Baby steps, Giant Steps
"""

import math


class Zp:
    def __init__(self, p):
        self.p = p

    def mul(self, a, b):
        return a * b % self.p

    def inv(self, a):
        for i in range(self.p):
            if self.mul(a, i) == 1:
                return i

    def q(self):
        return math.ceil(math.sqrt(self.p - 1))


def baby_steps(z, h, v):
    inv = z.inv(h)  # Multiplicative Inverse
    q = z.q()

    return {z.mul(inv**i, v): i for i in range(q)}


def giant_steps(z, h, v):
    q = z.q()

    precalc = baby_steps(z, h, v)

    for i in range(q):
        tmp = h**(i*q) % z.p

        # Exit condition
        if tmp in precalc.keys():
            return i * q + precalc[tmp]


def main():
    z = Zp(29)
    base = 11
    value = 3

    print(giant_steps(z, base, value))


if __name__ == "__main__":
    main()
