# https://fivethirtyeight.com/features/a-riddle-that-will-make-you-scream/
import time as t
from random import sample


def scream(cast_size=3):
    a = ["CC", "DA", "NC", "HB", "TH"]
    c = set(a[:cast_size])
    g = set(sample(a, cast_size))
    diff = len(c.difference(g))
    return diff <= 1


z = 0
runs = 999999 + 1
starter = t.time()

for i in range(runs):
    z = z + scream()

stopper = t.time()

print(f"{(z / runs):.2%}")
print(f"{(stopper - starter):.2f} seconds")

