# https://possiblywrong.wordpress.com/2019/01/09/identical-packs-of-skittles/

import numpy as np
import time


def skittles(flavors=5, mu=60, sigma=5):
    r = set()  # Sets cannot have dupes
    k: int = 0
    while len(r) == k:
        b: int = int(np.random.normal(mu, sigma, 1))
        d = tuple(
            np.bincount(
                np.random.randint(0, flavors, b)
            )
        )
        r.add(d)
        k = k + 1
    return k


def mean(lst):
    return sum(lst) / len(lst)


Z: list[int] = []
Q: float = 0

runs: int = 50000
burp: int = 100
rest: float = 0.5

for i in range(runs):
    j = i + 1
    Temp: int = skittles(5, 60, 5)
    Z.append(Temp)
    if j % burp == 0:
        Q = mean(Z)
        u = '{:,}/{:,} --> {:.2f}'.format(j, runs, Q)
        print(u)
        time.sleep(rest)


print(Q)
