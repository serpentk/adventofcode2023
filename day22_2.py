import sys

def match_xy(b1, b2):
    x1, y1, z1, x11, y11, z11 = b1
    x2, y2, z2, x21, y21, z21 = b2
    return (x2 <= x11 and x1 <= x21 and
            y2 <= y11 and y1 <= y21) 

def supports(b1, b2):
    """
    if b1 supports b2 (b2 stands on b1)
    """
    return b1[5] + 1 == b2[2] and match_xy(b1, b2)

def mark_brick(b, data, label):
    for jx in range(b[0], b[3] + 1):
        for jy in range(b[1], b[4] + 1):
            for jz in range(b[2], b[5] + 1):
                data[jz][jy][jx] = label


bricks = []
for i, line in enumerate(sys.stdin):
    begin, end = line.strip().split('~')
    bricks.append([int(x) for x in begin.split(',') + end.split(',')])
    assert((bricks[-1][0] <= bricks[-1][3] and
            bricks[-1][1] <= bricks[-1][4] and
            bricks[-1][2] <= bricks[-1][5]))

maxx = max([b[3] for b in bricks])
maxy = max([b[4] for b in bricks])
maxz = max([b[5] for b in bricks])

bricks.sort(key=lambda x: x[5])

data = []
for iz in range(maxz + 1):
    d = []
    for iy in range(maxy + 1):
        d.append([None] * (maxx + 1))
    data.append(d)

for i, b in enumerate(bricks):
    mark_brick(b, data, i)
                
for i, b in enumerate(bricks):
    newz = b[2]
    for z in range(b[2] - 1, 0, -1):
        if all([data[z][y][x] is None for x in range(b[0], b[3] + 1) for y in range(b[1], b[4] + 1)]):
            newz = z
        else:
            break
    mark_brick(b, data, None)
    b[2], b[5] = newz, newz + b[5] - b[2]
    mark_brick(b, data, i)

s = 0

children = {i: set() for i in range(len(bricks))}
supported_by = {i: {j for j in range(i) if supports(bricks[j], bricks[i])}
                for i in range(len(bricks))} 
supported = {i: {j for j in range(i, len(bricks)) if supports(bricks[i], bricks[j])}
                for i in range(len(bricks))}

parents = {i: set() for i in range(len(bricks))}
children = {i: set() for i in range(len(bricks))}

for i in range(len(bricks)):
    ps = supported_by[i]
    parents[i] = ps.copy()
    for p in ps:
        parents[i].update(parents[p])

for i in range(len(bricks) - 1, -1, -1):
    cn = supported[i]
    children[i] = cn.copy()
    for c in cn:
        children[i].update(children[c])

for i in range(len(bricks)):
    to_fall = {c for c in children[i]
               if all([(p == i or (p in children[i]) or (p in parents[i])) for p in parents[c]])}
    s += len(to_fall)

print(s)
