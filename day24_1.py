import sys
import numpy as np

b_min = 200000000000000
b_max = 400000000000000


def intersection(item1, item2):
    d = np.linalg.det(np.array([[item1[4], -item1[3]], [item2[4], -item2[3]]]))
    if d == 0:
        return None
    return (np.linalg.det(np.array([[item1[4] * item1[0] - item1[3] * item1[1], -item1[3]],
                                    [item2[4] * item2[0] - item2[3] * item2[1], -item2[3]]]))/d,
            np.linalg.det(np.array([[item1[4], item1[4] * item1[0] - item1[3] * item1[1]],
                                    [item2[4], item2[4] * item2[0] - item2[3] * item2[1]]]))/d
            )

def in_future(item, point):
    return (point[0] - item[0]) * item[3] >= 0 and (point[1] - item[1]) * item[4] >= 0 


data = []
for line in sys.stdin:
    position, vel = line.strip().split(' @ ')
    data.append([int(x) for x in position.split(', ') + vel.split(', ')])

s = 0
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        p = intersection(data[i], data[j])
        if (p is not None and
            p[0] <= b_max and p[1] <= b_max and p[0] >= b_min and p[1] >= b_min and
            in_future(data[i], p) and in_future(data[j], p)):
            s += 1

print(s)
                   
