
from random import sample

A = ["CC", "DA", "HB", "NC", "TH"]
cast_size = 3
# C = set(A[:cast_size])
C = set(A[:cast_size])
print(C)

g = sample(A, cast_size)

print(g)

delta = len(C.difference(g))
print(delta)

a = ["CC", "DA", "HB", "NC", "TH"]
c = set(a[:cast_size])
print(c)
