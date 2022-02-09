from random import sample


def urn_problem(b=20, w=20):
    q = b + w
    urn = ([0] * b) + ([1] * w)

    while q > 1:
        x = sample(urn, q)
        y = x[0] ^ 1
        try:
            z = x.index(y)
        except ValueError:
            z = 1
        urn = x[z:q]
        q = len(urn)
    return int(urn[0])


max_balls = 20
runs = 50000

for B in range(max_balls):
    for W in range(max_balls):
        Z = 0
        for i in range(runs):
            Temp = urn_problem(B+1, W+1)
            Z = Z + Temp
        print("B:{:} W:{:} --> {:.2%}".format(B+1, W+1, Z/runs))
