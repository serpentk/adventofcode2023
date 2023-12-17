import sys

blocks = []
for line in sys.stdin:
    blocks.append([int(c) for c in line.strip()])

def neighbors(x, y, dx, dy):
    res = []
    if dx >= 0:
        nbrs = [(x + d, y, dx + d, 0)
                for d in range(4, 11)
                if dx + d < 11 and x + d < len(blocks[0])]
        res.extend([n for n in nbrs if n not in visited])
    if dx <= 0:
        nbrs = [(x + d, y, dx + d, 0)
                for d in range(-10, -3)
                if dx + d > -11 and x + d >= 0]
        res.extend([n for n in nbrs if n not in visited])
    if dy >= 0:
        nbrs = [(x, y + d, 0, dy + d)
                for d in range(4, 11)
                if dy + d < 11 and y + d < len(blocks)]
        res.extend([n for n in nbrs if n not in visited])
    if dy <= 0:
        nbrs = [(x, y + d, 0, dy + d)
                for d in range(-10, -3)
                if dy + d > -11 and y + d >= 0]
        res.extend([n for n in nbrs if n not in visited])
    return res

visited = set()
results = {}

actual = {
     (0, 0, 0, 0): 0
}

while actual:
    if len(results) == 14: break
    closest_v = min(actual, key=actual.get)
    nbs = neighbors(*closest_v)
    if (closest_v[0], closest_v[1]) == (len(blocks[0]) - 1, len(blocks) - 1):
        results[closest_v] = actual[closest_v]
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

print(min(results.values()))
