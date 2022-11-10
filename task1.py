from pprint import pprint
numbers = list(range(0, 16))
keys = ['bin', 'dec', 'hex', 'oct']

values = []

for i in numbers:
    values.append([bin(i), i, hex(i), oct(i)])

d = [dict(zip(keys, sublist)) for sublist in values]
pprint(d)