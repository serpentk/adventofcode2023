import sys
sys.setrecursionlimit(10000)

hike_map = []
for line in sys.stdin:
    hike_map.append(line.strip())

xlen = len(hike_map[0])
y_len = len(hike_map)


def longest_hike(start, finish, avoid):
    x, y = start
    if hike_map[y][x] == '>':
        nbrs = [(x + 1, y)]
    elif hike_map[y][x] == '<':
        nbrs = [(x-1, y)]
    elif hike_map[y][x] == 'v':
        nbrs = [(x, y + 1)]
    elif hike_map[y][x] == '^':
        nbrs = [(x, y - 1)]
    else:
        nbrs = [(u, v)
                for (u, v) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                if hike_map[v][u] in ('.', '>', '<', 'v', '^')]
    nbrs = [nb for nb in nbrs if nb not in avoid]
    if not nbrs:
        res = None
    elif finish in nbrs:
        res = 1 + len(avoid)
    else:
        new_avoid = avoid.copy()
        new_avoid.add((x, y))
        hikes = [longest_hike(nb, finish, new_avoid) for nb in nbrs]
        hikes = [h for h in hikes if h is not None]
        if len(hikes) == 0:
            res = None
        else:
            res = max(hikes)
    return res

start = (hike_map[0].find('.'), 0)
finish = (hike_map[-1].find('.'), len(hike_map) - 1)
print(longest_hike((start[0], 1), finish, {start}))
