from random import sample

black = 3
white = 0

urn = ([0] * black) + ([1] * white)
q = len(urn)

# while q > 1:
x = sample(urn, q)
y = x[0] ^ 1
z = x.index(y) if y in x else q - 1
# https://stackoverflow.com/questions/12097033/python-index-error-value-not-in-list-on-indexvalue

print(x)
print(y)
print(z)
urn = x[z:q]
print(urn)
#     q = len(urn)
#
#
# print(int(urn[0]))