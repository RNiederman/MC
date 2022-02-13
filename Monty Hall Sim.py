import pandas as pd
import time as tm
from random import sample


def montey_hall(n_doors=3):
    choices = 2
    doors_to_open = n_doors - choices
    doors = range(n_doors)
    prize = set(sample(doors, 1))
    guess = set(sample(doors, 1))

    doors = set(doors)
    open_canidates = doors.difference(prize).difference(guess)
    opened = sample(list(open_canidates), doors_to_open)
    swap = doors.difference(guess).difference(opened)

    p, g, s = tuple(prize) + tuple(guess) + tuple(swap)
    return [(prize == guess), (prize == swap), p, g, s]


d = 3
trials = 5000
burp = 500
rest = .5

df = pd.DataFrame(columns=['Keep Win', 'Swap Win', 'Prize', "Guess", "Swap"])

for i in range(trials):
    z = montey_hall(d)
    df = df.append({'Keep Win': z[0], 'Swap Win': z[1],
                    'Prize': z[2], 'Guess': z[3], 'Swap': z[4]}, ignore_index=True)
    if i % burp == 0:
        print(f"{i:,}/{trials:,}")
        tm.sleep(rest)

print(df.to_string())

print(f"Keep Win Perc: {sum(df['Keep Win']/trials):.2%}")
print(f"Swap Win Perc: {sum(df['Swap Win']/trials):.2%}")
