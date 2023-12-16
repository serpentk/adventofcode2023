import sys


def next_tiles(x, y, direction, tile):
    if (tile == '.' or
        (tile == '-' and direction[1] == 0) or
        (tile == '|' and direction[0] == 0)):
        newx, newy = x + direction[0], y + direction[1]
        return ([(newx, newy, direction)] if (newx >= 0 and
                                              newy >= 0 and
                                              newx < len(tiles[0]) and
                                              newy < len(tiles)) else [])
    elif tile == '-':
        return [(x + d, y, (d, 0))
                for d in (-1, 1)
                if x + d >= 0 and x + d < len(tiles[0])]
    elif tile == '|':
        return [(x, y + d, (0, d))
                for d in (-1, 1)
                if y + d >= 0 and y + d < len(tiles)]
    else:
        if tile == '/':
            newdir = (-direction[1], -direction[0])
        else:
            newdir = (direction[1], direction[0])            
        newx, newy = x + newdir[0], y + newdir[1]
        return [(newx, newy, newdir)] if (newx >= 0 and
                                          newy >= 0 and
                                          newx < len(tiles[0]) and
                                          newy < len(tiles)) else []

                
tiles = []
for line in sys.stdin:
    tiles.append(line.strip())

visited = {(0, 0, (1, 0))}            
cur_tiles = {(0, 0, (1, 0))}

for step in range(4 * len(tiles) * len(tiles[0])):
    new_tiles = set()
    for p in cur_tiles:
        next_t = next_tiles(*p, tiles[p[1]][p[0]])
        next_t = [t for t in next_t if t not in visited]
        visited.update(next_t)
        new_tiles.update(next_t)
    if len(new_tiles) == 0:
        break
    cur_tiles = new_tiles
        

print(len({(x, y) for x, y, d in visited}))
