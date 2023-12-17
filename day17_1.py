import sys

blocks = []
for line in sys.stdin:
    blocks.append([int(c) for c in line.strip()])

def direction(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])


def allowed_directions(path):
    directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
    if len(path) > 3:
        last_dir = direction(path[-1], path[-2])
        if (last_dir == direction(path[-2], path[-3]) and
            last_dir == direction(path[-3], path[-4])):
            directions.remove(last_dir)
            directions.remove((-last_dir[0], -last_dir[1]))
    return directions
        

def allowed_next(path):
    x, y = p[-1]
    directions = allowed_directions(path)
    allowed = []
    if x > 0 and (-1, 0) in directions:
        allowed.append((x - 1, y))
    if y > 0 and (0, -1) in directions:
        allowed.append((x, y - 1))
    if x < len(blocks[0]) - 1 and (1, 0) in directions:
        allowed.append((x + 1, y))
    if y < len(blocks) - 1 and (0, 1) in directions:
        allowed.append((x, y + 1))
    return allowed


def neighbors(x, y, dx, dy):
    res = []
    if dx >= 0 and (x + 1, y, dx + 1, 0) in all_v:
        res.append((x + 1, y, dx + 1, 0))
    if dx <= 0 and (x - 1, y, dx - 1, 0) in all_v:
        res.append((x - 1, y, dx - 1, 0))
    if dy >= 0 and (x, y + 1, 0, dy + 1) in all_v:
        res.append((x, y + 1, 0, dy + 1))
    if dy <= 0 and (x, y - 1, 0, dy - 1) in all_v:
        res.append((x, y - 1, 0, dy - 1))
    return res

all_v = {
    (x, y, dx, dy)
    for x in range(len(blocks[0]))
    for y in range(len(blocks))
    for dy in range(max(y - len(blocks) + 1, -3), min(3, y) + 1)
    for dx in range(max(x - len(blocks[0]) + 1, -3), min(3, x) + 1)
    if dx * dy == 0 and dx + dy != 0
}

results = {}
for dx in range(1, 4): all_v.remove((0, 0, -dx, 0))
for dy in range(1, 4): all_v.remove((0, 0, 0, -dy))
all_v.add((0, 0, 0, 0))

actual = {
     (0, 0, 0, 0): 0
}

while actual:
    if len(results) == 6: break
    closest_v = min(actual, key=actual.get)
    nbs = neighbors(*closest_v)
    if (closest_v[0], closest_v[1]) == (len(blocks[0]) - 1, len(blocks) - 1):
        results[closest_v] = actual[closest_v]
    for v in nbs:
        x, y, dx, dy = v
        dist = actual[closest_v] + blocks[y][x]
        if v not in actual or actual[v] > dist: 
            actual[v] = dist
    del actual[closest_v]
    all_v.remove(closest_v)

print(min(results.values()))
