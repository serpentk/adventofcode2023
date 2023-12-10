import sys

pipes_map = []

def match_hor(left, right):
    return  (left in ('-', 'F', 'L', 'S') and
             right in('-', 'J', '7', 'S'))

def match_vert(top, bottom):
    return  (top in ('|', 'F', '7', 'S') and
             bottom in('|', 'J', 'L', 'S'))


def neighbors(pipes, x, y):
    ysize = len(pipes)
    xsize = len(pipes[0])
    res = []
    if x > 0 and match_hor(pipes[y][x - 1], pipes[y][x]):
        res.append((x - 1, y))
    if y > 0 and match_vert(pipes[y - 1][x], pipes[y][x]):
        res.append((x, y - 1))
    if x < xsize - 1 and match_hor(pipes[y][x], pipes[y][x + 1]):
        res.append((x + 1, y))
    if y < ysize - 1 and match_vert(pipes[y][x], pipes[y + 1][x]):
        res.append((x, y + 1))
    return res
        

def ring(paths):
    return [(i, j)
            for i in range(len(paths))
            for j in range(len(paths))
            if i != j and paths[i][-1] == paths[j][-1]]

def path(pipes):
    sy = [x for x, line in enumerate(pipes) if 'S' in line][0]
    sx = pipes[sy].find('S')
    paths = [[(sx, sy), (x, y)] for (x, y) in neighbors(pipes, sx, sy)]
    l = 1
    r = []
    while not r:
        l += 1
        for p in paths:
            next_tiles = [(x, y)
                          for x, y in neighbors(pipes, *p[-1])
                          if (x, y) != p[-2]]
            if not next_tiles:
                continue
            p.append(next_tiles[0])
            r = ring(paths)

    return paths[r[0][0]] + list(reversed(paths[r[0][1]][1:-1]))


def get_side(curside, curtile):
    if curtile in ('|', '-'):
        return curside
    if curtile in ('L', '7'):
        return {'l': 'b', 'r': 't', 't': 'r', 'b': 'l'}[curside]
    return {'l': 't', 'r': 'b', 't': 'l', 'b': 'r'}[curside]

def get_neighbor(x, y, side):
    delta = {'l': (-1, 0),
             'r': (1, 0),
             't': (0, -1),
             'b': (0, 1)}[side]
    return (x + delta[0], y + delta[1])


for line in sys.stdin:
    pipes_map.append(line.strip())

loop = path(pipes_map)

sx, sy = loop[0]
if {loop[1], loop[-1]} == {(sx, sy + 1), (sx, sy - 1)}:
    pipe = '|'
elif {loop[1], loop[-1]} == {(sx + 1, sy), (sx - 1, sy)}:
    pipe = '-'
elif {loop[1], loop[-1]} == {(sx, sy + 1), (sx - 1, sy)}:
    pipe = '7'
elif {loop[1], loop[-1]} == {(sx, sy + 1), (sx + 1, sy)}:
    pipe = 'F'
elif {loop[1], loop[-1]} == {(sx, sy - 1), (sx + 1, sy)}:
    pipe = 'L'
else:
    pipe = 'J'
pipes_map[sy] = pipes_map[sy].replace('S', pipe)

ysize = len(pipes_map)
xsize = len(pipes_map[0])
    
xmin = min([x for (x, y) in loop])
ymin = min([y for (x, y) in loop])
xmax = max([x for (x, y) in loop])
ymax = max([y for (x, y) in loop])

outside = {(x, y)
           for y in range(-1, ysize + 1)
           for x in list(range(-1, xmin)) + list(range(xmax + 1, xsize + 1))}.union(
    {(x, y)
     for x in range(-1, xsize + 1)
     for y in list(range(-1, ymin)) + list(range(ymax + 1, ysize + 1))
     })

loop_tiles = set(loop)

ystart = min([y for (x, y) in loop if x == xmin])
start = loop.index((xmin, ystart))

loop = loop[start:] + loop[:start]

x1, y1 = loop[1]
if x1 > xmin:
    side = 'l'
else:
    side = 't'

for x, y in loop:
    n1 = get_neighbor(x, y, side)
    newside = get_side(side, pipes_map[y][x])
    n2 = get_neighbor(x, y, newside)
    to_add = {n for n in (n1, n2) if n not in loop_tiles}
    side = newside
    outside.update(to_add)

for y in range(ysize):
    for x in range(xsize):
        if (x, y) in outside:
            neigborhood = [(i, j)
                           for i in range(x - 1, x + 2)
                           for j in range(y - 1, y + 2)
                           if (i, j) not in loop_tiles]
            outside.update(neigborhood)

checked = loop_tiles.union(outside)

print(len([(x, y)
           for x in range(xsize)
           for y in range(ysize)
           if (x, y) not in checked]))
            
