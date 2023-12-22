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

def can_support(b1, b2):
    """
    if b1 can support b2 (b2 can stand on b1)
    """
    return b2[2] >= b1[5] + 1 and match_xy(b1, b2)

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

    # print(data[jz][jy][jx])
                # assert data[jz][jy][jx] is None
                # data[jz][jy][jx] = i
for d in data:
    print(d)
                
for i, b in enumerate(bricks):
    newz = b[2]
    for z in range(b[2] - 1, 0, -1):
        #print('z={}: data={}, {}'.format(z, data[z]))
        if all([data[z][y][x] is None for x in range(b[0], b[3] + 1) for y in range(b[1], b[4] + 1)]):
            newz = z
        else:
            break
    print('Moving {} ({}) to {}'.format(b, i, newz))
    mark_brick(b, data, None)
    b[2], b[5] = newz, newz + b[5] - b[2]
    mark_brick(b, data, i)



    
    
# bricks.sort(key=lambda x: x[5])
# for b in bricks:    
#     print(b)
# print('------------------')

# for i, b in enumerate(bricks):
#     bottom = [b1 for b1 in bricks[:i] if can_support(b1, b)]
#     if bottom:
#         level = bottom[-1][5] + 1
#     else:
#         level = 1
#     print('Brick {} to level {}'.format(b, level))
#     b[2], b[5] = level, level + b[5] - b[2]
# for b in bricks:    
#      print(b)
# print('------------------')

s = 0
bricks.sort(key=lambda x: x[2])
for b in bricks:    
     print(b)
print('------------------')

for i, b in enumerate(bricks):
    print('{}: {}'.format(b, i))
    top = [b1 for b1 in bricks if supports(b, b1)]
    if (len(top) == 0 or
        all([len([b1 for b1 in bricks if supports(b1, t) and b1 != b]) > 0 for t in top])): 
        
        print('can do it')
        print(b, i)
        s += 1

print(len(bricks), s)
    
