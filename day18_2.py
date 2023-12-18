import sys
from enum import Enum

class Place(Enum):
    IN = 1
    OUT = 2
    BORDER = 3

def invert_place(p):
    if p == Place.IN: return Place.OUT
    if p == Place.OUT: return Place.IN
    return Place.Border


def intersections(dug_map, x):
    num_v = len(dug_cubes)
    res = []
    for i in range(num_v):
        x1, x2 = (min(dug_cubes[i][0], dug_cubes[(i + 1) % num_v][0]),
                  max(dug_cubes[i][0], dug_cubes[(i + 1) % num_v][0]))
        if  x > x1 and x < x2:
            res.append(dug_cubes[i][1])
    return sorted(res)


def detect_place(line, y):
    for k in sorted(list(line.keys())):
        if k[1] < y:
            continue
        if y >= k[0]:
            return line[k]
    return Place.OUT

cur = (0, 0)
dug_cubes = []
for line in sys.stdin:
    _, _, data = line.strip().split()
    direction = data[-2]
    n = int(data[2:-2], 16)
    if direction == '0':
        to_add = (cur[0] + n, cur[1])
    elif direction == '2':
         to_add = (cur[0] - n, cur[1])
    elif direction == '1':
         to_add = (cur[0], cur[1] + n)
    else:
         to_add = (cur[0], cur[1] - n)
    dug_cubes.append(to_add)
    cur = to_add

num_v = len(dug_cubes)
min_x = min([x[0] for x in dug_cubes])
max_x = max([x[0] for x in dug_cubes])
min_y = min([x[1] for x in dug_cubes])
max_y = max([x[1] for x in dug_cubes])

dug_cubes = [(x - min_x, y - min_y) for (x, y) in dug_cubes]
min_x = min([x[0] for x in dug_cubes])
max_x = max([x[0] for x in dug_cubes])
min_y = min([x[1] for x in dug_cubes])
max_y = max([x[1] for x in dug_cubes])

xs = sorted(list(set([p[0] for p in dug_cubes])))
by_x = {x: [(i, p) for i, p in enumerate(dug_cubes) if p[0] == x] for x in xs}

s = 0
line1 = dict()

for i, p in by_x[min_x]:
    if dug_cubes[(i + 1) % num_v][0] == min_x:
        y1, y2 = (min(p[1], dug_cubes[(i + 1) % num_v][1]),
                  max(p[1], dug_cubes[(i + 1) % num_v][1]))
        line1[(y1, y2)] = Place.BORDER
        s += y2 - y1 + 1

x = min_x + 1
cur_xvi = 1 if x in xs else 0
while x <= max_x:
    line = dict()
    line_s = 0
    # just intersections
    v_borders = intersections(dug_cubes, x)
    # long edges
    h_borders = {}
    if x in xs:
        for i, p in by_x[x]:
            if dug_cubes[(i + 1) % num_v][0] == x:
                y1, y2 = (min(p[1], dug_cubes[(i + 1) % num_v][1]),
                          max(p[1], dug_cubes[(i + 1) % num_v][1]))
                h_borders[y1] = y2
    ys = sorted(v_borders + list(h_borders.keys()))
    state = Place.OUT
    if ys[0] > min_y:
        line[(0, ys[0] - 1)] = state

    for iy, y in enumerate(ys):
        segment_end = ys[iy + 1] - 1 if iy < len(ys) - 1 else max_y
        if y in h_borders:
            line_s += h_borders[y] - y + 1
            line[(y, h_borders[y])] = Place.BORDER
            if detect_place(line1, y) != detect_place(line1, h_borders[y]):
                state = invert_place(state)
            y1 = h_borders[y] + 1
        else:
            line_s += 1
            line[(y, y)] = Place.BORDER
            state = invert_place(state)
            y1 = y + 1
        if y1 <= segment_end:
            line[(y1, segment_end)] = state            
            if state == Place.IN:
                line_s += segment_end - y1 + 1
    line1 = line
    if x in xs:
        s += line_s
        x += 1
        if x in xs: cur_xvi += 1
    else:
        s += line_s * (xs[cur_xvi + 1] - x)
        cur_xvi += 1
        x = xs[cur_xvi]

print(s)
    

        
    










