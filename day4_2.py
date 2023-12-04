# usage: python3 day4_2.py < testinput4.py

import fileinput

s = 0
cards = {}
for (n, line) in enumerate(fileinput.input()):
    _, data = line.split(': ')
    cardcount = cards.get(n, 1)
    s += cardcount
    winners, actual = data.split(' | ')
    winners = [int(x) for x in winners.split() if x]
    actual = [int(x) for x in actual.split() if x]
    won = len([x for x in actual if x in winners])
    for i in range(won):
        if n + i + 1 not in cards:
            cards[n + i + 1] = 1
        cards[n + i + 1] += cardcount

print(s)
