import sys

blocks = []
for line in sys.stdin:
    blocks.append([int(c) for c in line.strip()])

def neighbors(x, y, dx, dy):
    res = []
    if (x,y) == (0, 0) or dx:
        nbrs = [(x, y + d, 0, 1)
                for d in range(4, 11) if y + d < len(blocks)] + [
                        (x, y + d, 0, -1)
                        for d in range(-10, -3) if y + d >= 0]
        res.extend([n for n in nbrs if n not in visited])
        
    if (x,y) == (0, 0) or dy:
        nbrs = [(x + d, y, -1, 0)
                for d in range(-10, -3) if x + d >= 0] + [
                        (x + d, y, 1, 0)
                        for d in range(4, 11) if x + d < len(blocks[0])]
        res.extend([n for n in nbrs if n not in visited])

    return res

visited = set()

actual = {
     (0, 0, 0, 0): 0
}

while actual:
    closest_v = min(actual, key=actual.get)
    nbs = neighbors(*closest_v)
    if (closest_v[0], closest_v[1]) == (len(blocks[0]) - 1, len(blocks) - 1):
        print(actual[closest_v])
        break
    for v in nbs:
        x, y, dx, dy = v
        if dx:
            if x > closest_v[0]:
                xmin, xmax = closest_v[0] + 1, x
            else:
                xmin, xmax = x, closest_v[0] - 1
            dist = actual[closest_v] + sum([blocks[y][t] for t in range(xmin, xmax + 1)])
        else:
            if y > closest_v[1]:
                ymin, ymax = closest_v[1] + 1, y
            else:
                ymin, ymax = y, closest_v[1] - 1
            dist = actual[closest_v] + sum([blocks[t][x] for t in range(ymin, ymax + 1)])
        if v not in actual or actual[v] > dist: 
            actual[v] = dist
    del actual[closest_v]
    visited.add(closest_v)
