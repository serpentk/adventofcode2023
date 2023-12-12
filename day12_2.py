import sys
import re


def get_re(springs):
    replace_map = {'?': '.', '.': '\.', '#': '#'}
    return re.compile('^' + ''.join(replace_map[c] for c in springs) + '$')

def get_springs(valid, broken):
    return ''.join('.' * v + '#' * b for (v,b) in zip(valid, broken)) + '.' * v[-1]

def versions(n, spaces, first):
    if spaces == 1:
        yield [n]
    elif n >= spaces - 1:
        for x in range(0 if first else 1, n + 1):
            for v in versions(n - x, spaces - 1, False):
                yield [x] + v

s = 0
for line in sys.stdin:
    print(line.strip())
    springs, control = line.strip().split()
    control = list(map(int, control.split(',') * 5))
    springs = '?'.join([springs] * 5)
    r = get_re(springs)
    for v in versions(sum(control), len(control) + 1, True):
        # print(get_springs(v, control))
        if r.match(get_springs(v, control)):
            s += 1
print(s)
