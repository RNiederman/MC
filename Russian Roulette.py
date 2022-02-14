import time as tm
from random import sample


def russian_roulette(chambers=6):
    cylinder = range(2, chambers)
    bullet1 = sample(cylinder, 1)[0] - 1
    bullet2 = bullet1 + 1

    gun = [1] * chambers
    gun[bullet1] = 0
    gun[bullet2] = 0

    # No Spin
    ns = gun[1]

    # Spin
    ch = sample(range(0, chambers), 1)[0]
    sp = gun[ch]

    return[ns, sp]


trials = 25000
burp = 500
rest = .25

no_spin = 0
spin = 0


for i in range(trials):
    z = russian_roulette(6)
    no_spin = no_spin + z[0]
    spin = spin + z[1]

    if i % burp == 0:
        print(f"{i:,}/{trials:,}")
        tm.sleep(rest)

print(f"No Spin Win Perc: {no_spin/trials:.2%}")
print(f"Spin Win Perc: {spin/trials:.2%}")
