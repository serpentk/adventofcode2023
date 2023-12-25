import sys
from collections import Counter

def connected_size(nodes, node, deleted):
    visited = {node}
    to_visit = [n for n in nodes[node] if (n, node) not in deleted]
    while to_visit:
        new_to_visit = []
        visited.update(to_visit)
        for n in to_visit:
            new_to_visit.extend(
                [x for x in nodes[n] if (n, x) not in deleted and x not in visited])
        to_visit = new_to_visit
    return len(visited)

f = open('graph25.dot', 'w')
f.write('digraph {\n')
nodes = dict()
edges = []
for line in sys.stdin:
    v, vs = line.strip().split(':')
    vs = vs.strip().split()
    if v not in nodes:
        nodes[v] = []
    for item in vs:
        edges.append((v, item))        
        f.write('\t{} -> {}\n'.format(v, item))
        nodes[v].append(item)
        if item not in nodes:
            nodes[item] = [v]
        else:
            nodes[item].append(v)
f.write('}\n')
f.close()

# Now I can watch this awful graph and discover 3 required edges...
to_del = (('vgs', 'xjb'), ('ljl', 'xhg'), ('ffj', 'lkm'))
to_del = to_del + tuple(((v, u) for u, v in to_del))
s = connected_size(nodes, "vgs", to_del)
print(s * (len(nodes) - s))

