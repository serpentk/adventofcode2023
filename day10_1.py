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
        

def is_ring(paths):
    return bool([(i, j)
                 for i in range(len(paths))
                 for j in range(len(paths))
                 if i != j and paths[i][-1] == paths[j][-1]])

def farthest(pipes):
    sy = [x for x, line in enumerate(pipes) if 'S' in line][0]
    sx = pipes[sy].find('S')
    paths = [[(sx, sy), (x, y)] for (x, y) in neighbors(pipes, sx, sy)]
    l = 1
    while not is_ring(paths):
        l += 1
        for p in paths:
            next_tiles = [(x, y)
                          for x, y in neighbors(pipes, *p[-1])
                          if (x, y) != p[-2]]
            if not next_tiles:
                continue
            p.append(next_tiles[0])
    return l

  
for line in sys.stdin:
    pipes_map.append(line)


print(farthest(pipes_map))
