# usage: python3 day3_1.py testinput3.txt

import re
import sys

def is_symbol(c):
    return (c != '.' and not c.isdigit())

def line_sum(prevline, line, nextline):
    res = 0
    for match in re.finditer(r'\d+', line):
        start = max(match.start() - 1, 0)
        end = min(140, match.end() + 1)
        if any(map(is_symbol,
                   prevline[start : end] +
                   line[start : end] +
                   nextline[start : end])):
            res += int(match.group())
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
