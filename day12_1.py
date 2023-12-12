import sys
import re

def get_re(sizes):
    return re.compile(
        '^\.*' + '\.+'.join(['#{%s}' % x for x in sizes]) + '\.*$')

def versions(springs):
    if len(springs) == 0:
        yield ''
    else:
        if springs[0] == '?':
            cur = ('.', '#')
        else:
            cur = (springs[0],)
        for v in versions(springs[1:]):
            for c in cur:
                yield c + v

s = 0
for line in sys.stdin:
    springs, control = line.strip().split()
    r = get_re(control.split(','))
    for v in versions(springs):
        if r.match(v):
            s += 1
print(s)
