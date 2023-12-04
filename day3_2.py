# usage: python3 day3_2.py testinput3.txt

import re
import sys


def line_sum(prevline, line, nextline):
    res = 0
    prev_nums = list(re.finditer(r'\d+', prevline))
    line_nums = list(re.finditer(r'\d+', line))
    next_nums = list(re.finditer(r'\d+', nextline))
    for match in re.finditer(r'\*', line):
        matches = [m for m in prev_nums + line_nums + next_nums
                   if (m.start() < match.start() + 2 and
                       m.end() > match.start() - 1)]
        if len(matches) == 2:
            res += int(matches[0].group()) * int(matches[1].group())      
    return res

f = open(sys.argv[1])
emptyline = '.' * 140
prevline = f.readline()
line = f.readline()
s = line_sum(emptyline, prevline, line)
for nextline in f:
    s += line_sum(prevline, line, nextline)
    prevline, line = line, nextline
s += line_sum(prevline, line, emptyline)
print(s)
