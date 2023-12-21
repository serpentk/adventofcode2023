import sys

STEPS = 64
garden = []
actual = set()
for i, line in enumerate(sys.stdin):
    garden.append(line.strip())
    j = line.find('S')
    if j > -1:
        actual.add((j, i))

for step in range(STEPS):
    new_reached = set()
    for (xp, yp) in actual:
        nbrs = {(x, y)
                for x, y in ((xp + 1, yp), (xp - 1, yp), (xp, yp + 1), (xp, yp - 1))
                if (x >=0 and y >=0 and
                    x < len(garden[0]) and y < len(garden) and
                    garden[y][x] != '#')}
        new_reached.update(nbrs)
    actual = new_reached
        
print(len(actual))

