import pandas as pd
import time as tm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
from random import sample


# Build the Function for One Game
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


# Run the Game Muliple Times
maxx = 20
runs = 25000
df = pd.DataFrame(columns=['Blk', 'Wht', 'Prb', "RT"])

for b0 in range(maxx):
    b1 = b0 + 1
    for w0 in range(maxx):
        w1 = w0 + 1
        z = 0
        starter = tm.time()
        for j in range(runs):
            z = z + urn_problem(b1, w1)
        stopper = tm.time()
        print(f"B:{b1} W:{w1} --> {(z / runs):.2%}")
        df = df.append({'Blk': b1, 'Wht': w1, 'Prb': z / runs, 'RT': stopper - starter},
                       ignore_index=True)

print(df.to_string())

# Create a 3D Plot
g_title = "Yarrrr!!"
x_title = "Black Marbles"
y_title = "White Marbles"
z_title = "Prob of Not Dyin'"
graph_size = 8
big_font = 20
small_font = 12
color_map = "Greys"
ticks = list(
    range(int(maxx/10), maxx, int(maxx/10))
)

x = df['Blk']
y = df['Wht']
z = df['Prb']
color_key = np.array(x) - np.array(y)

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=color_key, cmap=color_map)

ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.zaxis.set_major_formatter(tk.PercentFormatter(xmax=1, decimals=None))

ax.set_title(g_title, fontsize=big_font)
ax.set_xlabel(x_title, fontsize=small_font)
ax.set_ylabel(y_title, fontsize=small_font)
ax.set_zlabel(z_title, fontsize=small_font)

ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

fig.set_size_inches(graph_size, graph_size)

plt.show()
