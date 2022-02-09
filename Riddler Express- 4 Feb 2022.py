# https://fivethirtyeight.com/features/a-riddle-that-will-make-you-scream/
from random import sample
import time as t


def scream(cast_size=3):
    a = ["CC", "DA", "HB", "NC", "TH"]
    c = set(sample(a, cast_size))
    g = set(sample(a, cast_size))
    diff = len(c.difference(g))
    return diff <= 1


Z = 0
runs = 999999 + 1
starter = t.time()

for i in range(runs):
    Q = scream()
    Z = Z + Q

stopper = t.time()

print("{:.2%}".format(Z / runs))
print("{:.2f} seconds".format(stopper - starter))
