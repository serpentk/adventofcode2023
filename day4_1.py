# usage: python3 day4_1.py < testinput4.py

import fileinput

s = 0
for line in fileinput.input():
    _, data = line.split(': ')
    winners, actual = data.split(' | ')
    winners = [int(x) for x in winners.split() if x]
    actual = [int(x) for x in actual.split() if x]
    won = [x for x in actual if x in winners]
    if won:
        s += pow(2, len(won) - 1)

print(s)
