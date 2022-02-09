import numpy as np

pack = np.random.binomial(100, 0.6)
draw = np.random.randint(0, 5, pack)
A = np.bincount(draw)
B = tuple(A)

print(pack)
print(draw)
print(A)
print(B)

#Q = tuple(np.bincount(np.random.randint(0, 5, np.random.binomial(100, 0.6))))
# print(Q)