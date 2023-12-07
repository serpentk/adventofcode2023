import collections
import sys

cards = {v: k
         for k, v in enumerate(['A', 'K', 'Q', 'J', 'T',
                                '9', '8', '7', '6', '5',
                                '4', '3', '2'])}

def hand_type(hand):
    c = collections.Counter(hand)
    if len(c) == 1: # Five of a kind
        return 0
    if c.most_common(1)[0][1] == 4: # Four of a kind
        return 1
    if len(c) == 2: # Full house
        return 2
    if c.most_common(1)[0][1] == 3: # Three of a kind
        return 3
    if len(c) == 3: # Two pair
        return 4
    if len(c) == 4: # One pair
        return 5
    return 6 # High card


hands = []
for line in sys.stdin:
    hands.append(line.split())

hands.sort(key=lambda x: [hand_type(x[0])] + [cards[c] for c in x[0]],
           reverse=True)

s = 0
for r, bid in enumerate([int(h[1]) for h in hands]):
    s += (r + 1) * bid

print(s)

