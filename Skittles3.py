# https://possiblywrong.wordpress.com/2019/01/09/identical-packs-of-skittles/
# https://gist.github.com/possibly-wrong/2e33f6c137383b896474daa53d72daab
import numpy as np
import time as tm

def skittles(flavors=5, pack_size=60):
    p = pack_size/100
    packs = set()
    count = 0
    while len(packs) == count:
        packs.add(tuple(np.bincount(
            np.random.randint(0, flavors, np.random.binomial(100, p)))))
        count = count + 1
    return count


breaker: int = 25000
updater: int = 1000
rest: float = 0.5

total: int = 0
num_samples: int = 0

while num_samples < breaker:
    total = total + skittles(5, 60)
    num_samples = num_samples + 1
    if num_samples % updater == 0:
        print(f"{num_samples:,} / {breaker:,} --> {total / num_samples:.2f}")
        tm.sleep(rest)

print('{:.2f}'.format(total / num_samples))
