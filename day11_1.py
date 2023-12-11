import sys

space = []
galaxies = []
empty_rows = []
for (i, line) in enumerate(sys.stdin):
    print(line.strip())
    space.append([c for c in line.strip()])
    g = [j for j, c in enumerate(line) if c == '#']
    galaxies.extend([(i, j) for j in g])
    if len(g) == 0:
        empty_rows.append(i)

empty_cols = []
for j in range(len(space[0])):
    if not any([row[j] == '#' for row in space]):
        empty_cols.append(j)

s = 0

for i, g in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
        c = len([c for c in empty_cols
                 if c < max(g[1], galaxies[j][1]) and c > min(g[1], galaxies[j][1])])
        r = len([r for r in empty_rows
                 if r < max(g[0], galaxies[j][0]) and r > min(g[0], galaxies[j][0])])
        s += abs(g[0] - galaxies[j][0]) + abs(g[1] - galaxies[j][1]) + r + c

print(s)
