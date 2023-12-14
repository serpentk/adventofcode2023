import sys

rocks = []

for n, line in enumerate(sys.stdin):
    rocks.append(list(line.strip()))
    for i in range(len(rocks[0])):
        if rocks[n][i] in ('#', '.'): continue
        dest = 0
        for j in range(n-1, -1, -1):
            if rocks[j][i] in ('O', '#'):
                dest = j + 1
                break
        rocks[n][i] = '.'
        rocks[dest][i] = 'O'

s = 0
for i in range(len(rocks)):
    s += len([x for x in rocks[i] if x == 'O']) * (len(rocks) - i)

print(s)
            
