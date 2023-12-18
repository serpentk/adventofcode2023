import sys

cur = (0, 0)
dug_cubes = set()
for line in sys.stdin:
    direction, n, _ = line.strip().split()
    n = int(n)
    if direction == 'R':
        to_add = [(cur[0] + t + 1, cur[1]) for t in range(n)]
    elif direction == 'L':
         to_add = [(cur[0] - t - 1, cur[1]) for t in range(n)]
    elif direction == 'D':
         to_add = [(cur[0], cur[1] + t + 1) for t in range(n)]
    else:
         to_add = [(cur[0], cur[1] - t - 1) for t in range(n)]
    dug_cubes.update(to_add)
    cur = to_add[-1]

min_x = min([x[0] for x in dug_cubes])
max_x = max([x[0] for x in dug_cubes])
min_y = min([x[1] for x in dug_cubes])
max_y = max([x[1] for x in dug_cubes])

outside = set(
    [(a, b) for a, b in (
        [(min_x, y) for y in range(min_y, max_y + 1)] +
        [(max_x, y) for y in range(min_y, max_y + 1)] +
        [(x, min_y) for x in range(min_x, max_x + 1)] +
        [(x, max_y) for x in range(min_x, max_x + 1)])
     if (a, b) not in dug_cubes])

delta = len(outside)
cur_out = outside
while delta:
    to_add = set()
    for p in cur_out:
        nbr = []
        if p[0] < max_x:
            nbr.append((p[0] + 1, p[1]))
        if p[0] > min_x:
            nbr.append((p[0] - 1, p[1]))
        if p[1] < max_y:
            nbr.append((p[0], p[1] + 1))
        if p[1] > min_y:
            nbr.append((p[0], p[1] - 1))
        to_add.update([t for t in nbr
                       if (t not in dug_cubes) and (t not in outside)])
    delta = len(to_add)
    cur_out = to_add
    outside.update(to_add)

print((max_x - min_x +1) * (max_y - min_y + 1) - len(outside))
    
