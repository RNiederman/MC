# https://possiblywrong.wordpress.com/2019/01/09/identical-packs-of-skittles/

import numpy as np
from random import choices
from collections import Counter
import time


def skittles(mu=60, sigma=5):
    flavors = ["S", "O", "L", "A", "G"]
    r: list[str] = []
    m = False

    while not m:
        bag: int = int(np.random.normal(mu, sigma, 1))
        draw: list[str] = choices(flavors, k=bag)
        e1 = Counter(draw)
        e2 = sorted(e1.items())
        e3 = ' '.join(map(str, e2))
        m = e3 in r
        r.append(e3)
    return len(r)


def mean(lst):
    return sum(lst) / len(lst)


Z: list[int] = []
Q: float = 0

runs: int = 25000
burp: int = 1000
rest: float = 0.5

for i in range(runs):
    j = i + 1
    Temp: int = skittles(60, 5)
    Z.append(Temp)
    if j % burp == 0:
        Q = mean(Z)
        u = '{:,}/{:,} --> {:.2f}'.format(j, runs, Q)
        print(u)
        time.sleep(rest)

print(Q)
