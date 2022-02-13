# https://possiblywrong.wordpress.com/2019/01/09/identical-packs-of-skittles/
import numpy as np
import time as tm


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


z: list[int] = []
q: float = 0

runs: int = 25000
burp: int = 1000
rest: float = 0.5

for i in range(runs):
    j = i + 1
    temp: int = skittles(5, 60, 5)
    z.append(temp)
    if j % burp == 0:
        q = mean(z)
        print(f"{j:,}/{runs:,} --> {q:.2f}")
        tm.sleep(rest)

q = mean(z)
print(q)
