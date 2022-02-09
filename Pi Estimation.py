# Import Stuff
import numpy as np
import math

Rad: int = 5
NegRad: int = Rad * -1

n: int = 999999 + 1
multi = 25
n = int(n * multi)

x = np.random.uniform(low=NegRad, high=Rad, size=n)
y = np.random.uniform(low=NegRad, high=Rad, size=n)

Tester: bool = x ** 2 + y ** 2 <= Rad ** 2
CirPerc = sum(Tester) / n

SqArea = (2 * Rad) ** 2
CirArea = SqArea * CirPerc

p = CirArea / Rad ** 2
delta = abs(math.pi - p)

print(math.pi)
print(p)
print(delta)