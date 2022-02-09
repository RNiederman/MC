Actors = ["CC", "DA", "HB", "NC", "TH"]
cast_size = 3
Cast: list[str] = Actors[:2]
Cast.append(Actors[3])
#
# n: int = 0
# guess: list[str] = ["CC", "DA", "TH"]
# for j in range(cast_size):
#     b = guess[j] in Cast
#     print(b)
#     n = n + b
#
# print(n)

guess: list[str] = ["CC", "DA", "TH"]
check = sum(elem in guess for elem in Cast)
print(check)
print(Cast)
print(guess)
