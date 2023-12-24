import sys
sys.setrecursionlimit(10000)

hike_map = []
for line in sys.stdin:
    hike_map.append(line.strip())
start = (hike_map[0].find('.'), 0)
finish = (hike_map[-1].find('.'), len(hike_map) - 1)

node_map = {start: {}, finish: {}}

xlen = len(hike_map[0])
ylen = len(hike_map)


def step(prev, start):
    if start == finish:
        return start, None
    x, y = start
    nbrs = [(u, v)
            for (u, v) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            if hike_map[v][u] in ('.', '>', '<', 'v', '^') and (u, v) != prev]
    if len(nbrs) == 1:
        return start, nbrs[0]
    return start, None
    

def follow_edge(prev, start):
    if prev in node_map and start in node_map[prev]:
        return node_map[prev][start]
    else:
        if prev not in node_map: node_map[prev] = {}
    s = 0
    p, cur = prev, start
    while cur:
        s += 1
        p, cur = step(p, cur)
    if p not in node_map:
        x, y = p
        nbrs = [(u, v)
                for (u, v) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                if hike_map[v][u] in ('.', '>', '<', 'v', '^')]
        if len(nbrs) == 0:
            p = None
        else:
            node_map[p] = {}
    res = p, s
    node_map[prev][start] = res
    return res
        

def longest_hike(start, finish, avoid, curlen):
    if start == finish:
        return curlen
    x, y = start
    nbrs = [(u, v)
            for (u, v) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            if hike_map[v][u] in ('.', '>', '<', 'v', '^')]

    nbrs = [nb for nb in nbrs if nb not in avoid]
    if not nbrs:
        res = None
    elif finish in nbrs:
        res = 1 + curlen
    else:
        new_avoid = avoid.copy()
        new_avoid.add(start)

        nb_nodes = [follow_edge(start, nb) for nb in nbrs]
        nb_nodes = [nb for nb in nb_nodes if nb[0] is not None and nb[0] not in avoid]

        hikes = [longest_hike(nb[0], finish, new_avoid, curlen + nb[1]) for nb in nb_nodes]
        hikes = [h for h in hikes if h is not None]
        if len(hikes) == 0:
            res = None
        else:
            res = max(hikes)
    return res

print(longest_hike((start[0], 1), finish, {start}, 1))
