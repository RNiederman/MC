from random import sample
import pandas as pd
import time as t
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick


def urn_problem(black=20, white=20):

    urn = ([0] * black) + ([1] * white)
    q = len(urn)

    while q > 1:
        d = sample(urn, q)
        m = d[0] ^ 1
        i = d.index(m) if m in d else q - 1
        urn = d[i:]
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
        for j in range(runs):
            Z = Z + urn_problem(B, W)
        stopper = t.time()
        print("B:{:} W:{:} --> {:.2%}".format(B, W, Z / runs))
        df = df.append({'Blk': B, 'Wht': W, 'Prb': Z / runs, 'RT': stopper - starter},
                       ignore_index=True)

print(df.to_string())

# Create a 3D Plot
Graph_Title = "Yarrrr!!"
X_Title = "Black Marbles"
Y_Title = "White Marbles"
Z_Title = "Prob of Not Dyin'"
Graph_Size = 8
BigFont = 20
SmallFont = 12
ColorMap = "Greys"
tickers = list(
    range(int(MaxM/10), MaxM, int(MaxM/10))
)

x = df['Blk']
y = df['Wht']
z = df['Prb']
ColorKey = np.array(x) - np.array(y)

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=ColorKey, cmap=ColorMap)

ax.set_xticks(tickers)
ax.set_yticks(tickers)
ax.zaxis.set_major_formatter(tick.PercentFormatter(xmax=1, decimals=None))

ax.set_title(Graph_Title, fontsize=BigFont)
ax.set_xlabel(X_Title, fontsize=SmallFont)
ax.set_ylabel(Y_Title, fontsize=SmallFont)
ax.set_zlabel(Z_Title, fontsize=SmallFont)

ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

fig.set_size_inches(Graph_Size, Graph_Size)

plt.show()
