import sys

galaxies = []
empty_rows = []
rowlen = None
for (i, line) in enumerate(sys.stdin):
    rowlen = len(line.strip())
    g = [j for j, c in enumerate(line) if c == '#']
    galaxies.extend([(i, j) for j in g])
    if len(g) == 0:
        empty_rows.append(i)

empty_cols = []
for j in range(rowlen):
    if not any([g[1] == j for g in galaxies]):
        empty_cols.append(j)

s = 0
expanse = 1000000

for i, g in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
        c = len([c for c in empty_cols
                 if c < max(g[1], galaxies[j][1]) and c > min(g[1], galaxies[j][1])])
        r = len([r for r in empty_rows
                 if r < max(g[0], galaxies[j][0]) and r > min(g[0], galaxies[j][0])])
        s += abs(g[0] - galaxies[j][0]) + abs(g[1] - galaxies[j][1]) + (r + c) * (expanse - 1)

print(s)
