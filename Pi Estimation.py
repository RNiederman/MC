import numpy as np
import math

rad: int = 5
neg_rad: int = rad * -1

n: int = 999999 + 1
multi: float = 1
n = int(n * multi)

x = np.random.uniform(low=neg_rad, high=rad, size=n)
y = np.random.uniform(low=neg_rad, high=rad, size=n)

tester: bool = x ** 2 + y ** 2 <= rad ** 2
cir_perc: float = sum(tester) / n

sq_area: float = (2 * rad) ** 2
cir_area: float = sq_area * cir_perc

p: float = cir_area / rad ** 2
delta: float = abs(math.pi - p)

print(math.pi)
print(p)
print(delta)
