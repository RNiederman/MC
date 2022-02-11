from random import sample
import pandas as pd
import time as t


def urn_problem(black=20, white=20):

    urn = ([0] * black) + ([1] * white)
    q = len(urn)

    while q > 1:
        x = sample(urn, q)
        y = x[0] ^ 1
        z = x.index(y) if y in x else q - 1
        urn = x[z:]
        q = len(urn)

    return int(urn[0])
    # 1 you live, 0 you die


MaxM = 20
runs = 25000
df = pd.DataFrame(columns=['Blk', 'Wht', 'Prb', "RT"])

for b in range(MaxM):
    B = b + 1
    for w in range(MaxM):
        W = w + 1
        Z = 0
        starter = t.time()
        for i in range(runs):
            Z = Z + urn_problem(B, W)
        stopper = t.time()
        print("B:{:} W:{:} --> {:.2%}".format(B, W, Z / runs))
        df = df.append({'Blk': B, 'Wht': W, 'Prb': Z / runs, 'RT': stopper - starter},
                       ignore_index=True)

print(df.to_string())
