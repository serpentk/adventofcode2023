import sys
import re

def get_springs(valid, broken):
    return ''.join('.' * v + '#' * b for (v,b) in zip(valid, broken)) + '.' * valid[-1]

def match_c(c0, c):
    if c0 == '?':
        return True
    return c == c0

def match(template, springs):
    return all([match_c(c, springs[i]) for i, c in enumerate(template)])


cache = {}
            
def versions_count(n, spaces, first, broken, template):
    #print(n, spaces, first, broken, template)
    vc = cache.get((n, spaces, first, tuple(broken), template))
    if vc is not None:
        return vc
    
    if spaces == 1:
        if (n == 0 or match(template[-n:], '.' * n)):
            vc = 1
        else:
            vc = 0
    elif n >= spaces - (2 if first else 1):
        vc = 0
        for x in range(0 if first else 1, n + 1):
            if (match(template[:x + broken[0]], '.' * x + '#' * broken[0])):
                vc += versions_count(n - x, spaces - 1, False, broken[1:], template[(x + broken[0]):])
    else:
        vc = 0
    cache[(n, spaces, first, tuple(broken), template)] = vc
    return vc
    
            
s = 0
for line in sys.stdin:
    springs, control = line.strip().split()
    control = list(map(int, control.split(',') * 5))
    springs = '?'.join([springs] * 5)
    s += versions_count(len(springs) - sum(control), len(control) + 1, True, control, springs)
print(s)
