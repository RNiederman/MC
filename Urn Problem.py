from random import sample
import pandas as pd
import time as t
import matplotlib.pyplot as plt


def urn_problem(black=20, white=20):

    urn = ([0] * black) + ([1] * white)
    q = len(urn)

    while q > 1:
        draw = sample(urn, q)
        diff = draw[0] ^ 1
        marker = draw.index(diff) if diff in draw else q - 1
        urn = draw[marker:]
        q = len(urn)

    return int(urn[0])
    # 1 you live, 0 you die


MaxM = 20
runs = 25000
df = pd.DataFrame(columns=['Blk', 'Wht', 'Prb', "Delta", "RT"])

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
        df = df.append({'Blk': B, 'Wht': W, 'Prb': Z / runs, 'Delta': B-W, 'RT': stopper - starter},
                       ignore_index=True)

print(df.to_string())

# Create a 3D Plot
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')

x = df.iloc[:, 0]
y = df.iloc[:, 1]
z = df.iloc[:, 2]
ColorKey = df.iloc[:, 3]
ColorMap = "Greys"
ax.scatter(x, y, z, c=ColorKey, cmap=ColorMap)

ticks = list(range(2, MaxM, 2))
ax.set_xticks(ticks)
ax.set_yticks(ticks)

BigFont = 20
SmallFont = 12
ax.set_title("Yarrrr!", fontsize=BigFont)
ax.set_xlabel("Black Marbles", fontsize=SmallFont)
ax.set_ylabel("White Marbles", fontsize=SmallFont)
ax.set_zlabel("Prob of Not Dyin'", fontsize=SmallFont)

size = 8
fig.set_size_inches(size, size)

plt.show()
