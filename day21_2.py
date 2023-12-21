import sys
import collections

STEPS = 26501365
garden = []


def reached(startx, starty):
    res = []
    actual = {(startx, starty)}
    res.append(len(actual))
    for step in range(len(garden) + len(garden[0]) - 1):
        new_reached = set()
        for (xp, yp) in actual:
            nbrs = {(x, y)
                    for x, y in ((xp + 1, yp), (xp - 1, yp), (xp, yp + 1), (xp, yp - 1))
                    if (x >=0 and y >=0 and
                        x < len(garden[0]) and y < len(garden) and
                        garden[y][x] != '#')}
            new_reached.update(nbrs)
        actual = new_reached
        res.append(len(actual))
    return res


start = None
for i, line in enumerate(sys.stdin):
    garden.append(line.strip())
    j = line.find('S')
    if j > -1:
        start = (i, j)


print(len(garden[0]), len(garden))
cycles = {s : reached(*s)
          for s in (start,
                    (0, start[1]),
                    (len(garden[0]) - 1, start[1]),
                    (start[0], 0),
                    (start[0], len(garden) - 1),
                    (0, 0),
                    (len(garden[0]) - 1, 0),
                    (len(garden[0]) - 1, len(garden) - 1),
                    (0, len(garden) - 1))}

print(cycles[(65, 65)][261] * 202299 * 202299 +
      cycles[(65, 65)][260] * 202300 * 202300 +
      cycles[(65, 130)][130] + cycles[(65, 0)][130] +  cycles[(130, 65)][130] + cycles[(0, 65)][130] +
      202300 * (
          cycles[(0, 130)][64] + cycles[(130, 0)][64] + cycles[(0, 0)][64] + cycles[(130, 130)][64]) +
      202299 * (
          cycles[(0, 130)][195] + cycles[(130, 0)][195] + cycles[(0, 0)][195] + cycles[(130, 130)][195])
      )
