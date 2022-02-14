import time as tm
from random import choices


def craps():
    sides = 6
    die = range(1, sides + 1)
    opener = sum(choices(die, k=2))
    # hp = [0, 1,  2,  3, 4, 5, 6,  7, 8, 9, 10, 11, 12]
    key1 = [0, 0, -1, -1, 0, 0, 0,  1, 0, 0,  0,  1,  0]
    key2 = [0, 0,  0,  0, 0, 0, 0, -1, 0, 0,  0,  0,  0]
    check = key1[opener]

    key2[opener] = 1
    while check == 0:
        roll = sum(choices(die, k=2))
        check = key2[roll]
    do_not_pass = 0 if opener == 12 else -1 * check
    return [check, do_not_pass]


trials = 999999 + 1
burp = 50000
rest = .25

p = 0
dnp = 0

for i in range(trials):
    z = craps()
    p = p + z[0]
    dnp = dnp + z[1]

    if i % burp == 0:
        print(f"{i:,}/{trials:,}")
        tm.sleep(rest)

print(f"Pass Winnings: ${p:,}")
print(f"Do Not Pass Winnings: ${dnp:,}")
