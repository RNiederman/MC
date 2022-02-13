# https://possiblywrong.wordpress.com/2019/01/09/identical-packs-of-skittles/
import numpy as np
import time as tm
from random import choices
from collections import Counter


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


z: list[int] = []
q: float = 0

runs: int = 25000
burp: int = 1000
rest: float = 0.5

for i in range(runs):
    j = i + 1
    temp: int = skittles(60, 5)
    z.append(temp)
    if j % burp == 0:
        q = mean(z)
        print(f"{j:,}/{runs:,} --> {q:.2f}")
        tm.sleep(rest)

q = mean(z)
print(q)
